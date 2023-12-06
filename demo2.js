var w=800;
var h=400;
var jugador;
var fondo;

var bala, balaD = false, nave;

var salto;
var menu;
var sonido;

var velocidadBala;
var despBala;
var despBala2;
var estatusAire;
var estatuSuelo;

//bala 2
var bala2;
var bala2D = false;

//controles horizontales
var botones;

var estatusLeft;
var estatusRight;

//CSV
var rows = [
	[
		"despBala",
		"velocidadBala",
		"despBala2",
		"estatusAire",
		"estatusLeft",
		"estatusRigth",
	],
];

var nnNetwork , nnEntrenamiento, nnSalida, datosEntrenamiento=[];
var modoAuto = false, eCompleto = false;


var juego = new Phaser.Game(w, h, Phaser.CANVAS, '', { preload: preload, create: create, update: update, render:render});

function preload() {
    juego.load.image('fondo', 'assets/game/fondo.jpg');
    juego.load.spritesheet('mono', 'assets/sprites/altair.png',32 ,48);
    juego.load.image('nave', 'assets/game/ufo.png');
    juego.load.image('bala', 'assets/sprites/purple_ball.png');
    juego.load.image('menu', 'assets/game/menu.png');
    juego.load.audio('jumpSound', 'assets/audio/jump.mp3');
}

function create() {

    juego.physics.startSystem(Phaser.Physics.ARCADE);
    juego.physics.arcade.gravity.y = 800;
    juego.time.desiredFps = 30;

    fondo = juego.add.tileSprite(0, 0, w, h, 'fondo');
    nave = juego.add.sprite(w-100, h-70, 'nave');
    bala = juego.add.sprite(w-100, h, 'bala');
    bala2 = juego.add.sprite(w - 750, h - 400, 'bala');
    jugador = juego.add.sprite(50, h, 'mono');


    juego.physics.enable(jugador);
    jugador.body.collideWorldBounds = true;
    var corre = jugador.animations.add('corre',[8,9,10,11]);
    jugador.animations.play('corre', 10, true);

    juego.physics.enable(bala);
    bala.body.collideWorldBounds = true;

    juego.physics.enable(bala2);
    bala2.body.collideWorldBounds = true;

    pausaL = juego.add.text(w - 100, 20, 'Pausa', { font: '20px Arial', fill: '#fff' });
    pausaL.inputEnabled = true;
    pausaL.events.onInputUp.add(pausa, self);
    juego.input.onDown.add(mPausa, self);

    salto = juego.input.keyboard.addKey(Phaser.Keyboard.SPACEBAR);
    sonido = juego.sound.add('jumpSound');


    botones = juego.input.keyboard.createCursorKeys();
    
    nnNetwork =  new synaptic.Architect.Perceptron(3,10,3,3);
    nnEntrenamiento = new synaptic.Trainer(nnNetwork);

}

function enRedNeural(){
    nnEntrenamiento.train(datosEntrenamiento, {log: 1000, rate: 0.0003, iterations: 10000, shuffle: true});
}


function datosDeEntrenamiento(param_entrada) {
	console.log(
		"Entrada",
		param_entrada[0] + " " + param_entrada[1] + " " + param_entrada[2]
	);
    nnSalida = nnNetwork.activate(param_entrada);
	console.log("NNSALIDA");
	console.log(nnSalida);
	return [nnSalida[0] > 0.5 ? 1 : 0, nnSalida[1], nnSalida[2]];
}



function pausa() {
    restartGame();
    juego.paused = true;
    menu = juego.add.sprite(w/2,h/2, 'menu');
    menu.anchor.setTo(0.5, 0.5);
}

function mPausa(event){
    if (juego.paused) {
        var menu_x1 = w/2 - 270/2, menu_x2 = w/2 + 270/2,
            menu_y1 = h/2 - 180/2, menu_y2 = h/2 + 180/2;

        var mouse_x = event.x  ,
            mouse_y = event.y  ;

        if(mouse_x > menu_x1 && mouse_x < menu_x2 && mouse_y > menu_y1 && mouse_y < menu_y2 ){
            if(mouse_x >=menu_x1 && mouse_x <=menu_x2 && mouse_y >=menu_y1 && mouse_y <=menu_y1+90){
                eCompleto=false;
                datosEntrenamiento = [];
                modoAuto = false;
            }else if (mouse_x >=menu_x1 && mouse_x <=menu_x2 && mouse_y >=menu_y1+90 && mouse_y <=menu_y2) {
                if(!eCompleto) {
                    console.log("","Entrenamiento con: "+ datosEntrenamiento.length +" valores" );
                    enRedNeural();
                    eCompleto=true;
                }
                modoAuto = true;
            }

            menu.destroy();
            resetVariables();
            juego.paused = false;

        }
    }
}


function resetVariables() {
    // jugador.body.velocity.x = 0;
    // jugador.body.velocity.y = 0;
    bala.body.velocity.x = 0;
    bala.position.x = w - 100;
    balaD = false;
}

function resetBala2() {
    bala2.body.velocity.x = 0;
    bala2.position.x = jugador.body.position.x;
	bala2.position.y = 0;
	bala2D = false;
}

function restartGame() {
    jugador.body.position.x = 50;
	jugador.body.position.y = h;
	jugador.body.velocity.x = 0;
    jugador.body.velocity.y = 0;
    
	bala.body.velocity.x = 0;
	bala.position.x = w - 100;
	balaD = false;

	bala2.body.velocity.x = 0;
	bala2.position.x = jugador.body.position.x;
	bala2.position.y = 0;
	bala2D = false;
}


function saltar() {
    sonido.play();
    jugador.body.velocity.y = -270;
}

function moveRight() {
    jugador.body.velocity.x = 150
    estatusLeft = 0;
	estatusRight = 1;
}

function moveLeft() {
    jugador.body.velocity.x = -150
    estatusLeft = 1;
	estatusRight = 0;
}

function juegoManual() {
    jugador.body.velocity.x = 0;
	estatusLeft = 0;
	estatusRight = 0;
    if(salto.isDown && jugador.body.onFloor() ){
        saltar();
    }

    if (botones.right.isDown ){
        moveRight();
    }

    if (botones.left.isDown ){
        moveLeft();
    }
}

function juegaIA() {
    if (bala.position.x > 0) {
        jugador.body.velocity.x = 0;
	    estatusLeft = 0;
	    estatusRight = 0;
        var data = datosDeEntrenamiento([despBala, velocidadBala, despBala2])
        console.log("DATA: ");
		console.log(data);
        if (data[0]) {
            if (jugador.body.onFloor()) {
                saltar();
            }
		}
		if (data[1] > data[2]) {
            moveLeft();  
		}
        if (data[2] > data[1]) {
            moveRight();
		}
	}
}


function update() {

    fondo.tilePosition.x -= 1; 

    juego.physics.arcade.collide(bala, jugador, colisionH, null, this);

    juego.physics.arcade.collide(bala2, jugador, colisionH, null, this);

    estatuSuelo = 1;
    estatusAire = 0;

    if(!jugador.body.onFloor()) {
        estatuSuelo = 0;
        estatusAire = 1;
    }
	
    despBala = Math.floor( jugador.position.x - bala.position.x );
    despBala2 = Math.floor(jugador.position.x - bala2.position.x);
    
    if (modoAuto == false) {
        juegoManual();
    }
    else{
        juegaIA();
    }

    if( balaD==false ){
        disparo();
    }

    if( bala.position.x <= 0  ){
        resetVariables();
    }
    
    if (bala2.position.y >= 383) {
        resetBala2();
    }
    
    //entender
    if (modoAuto == false && bala.position.x > 0) {
		rows.push([
			despBala,
			velocidadBala,
			despBala2,
			estatusAire,
			estatusLeft,
			estatusRight,
		]);
		datosEntrenamiento.push({
			input: [despBala, velocidadBala, despBala2],
			output: [estatusAire, estatusLeft, estatusRight],
		});
		console.log(
			`Bala 1: ${despBala}, Bala 1 Velocidad: ${velocidadBala}, Bala 2: ${despBala2}, Estatus Aire: ${estatusAire}, EstatusIzquierda: ${estatusLeft}, EstatusDerecha: ${estatusRight}`
		);
	}
}


function disparo(){
    velocidadBala = -1 * velocidadRandom(300, 800);
    bala.body.velocity.y = 0 ;
    bala.body.velocity.x = velocidadBala;
    balaD=true;
}


function colisionH() {
    pausa();

    var csvContent =
		"data:text/csv;charset=utf-8," +
		rows.map((e) => e.join(",")).join("\n");
    var encodedUri = encodeURI(csvContent);
    window.open(encodedUri);
    
}

function velocidadRandom(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function render(){

}
