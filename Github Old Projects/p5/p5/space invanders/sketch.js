var ship;
var aliens = [];
var shots = [];
//var alien;
function setup() {
  // put setup code here
createCanvas(600,400);
ship = new Ship();
//alien = new Alien(width/2,80);
for(var i = 0; i < 6; i++){
	aliens[i] = new Alien(i*80 + 80, 60);
console.log("NEW ALIEN SAVE YOURSELF! :( ");
}
  }

function draw() {
  // put drawing code here
  background(0);
//alien.show();
  ship.show();


  for(var i = 0; i < aliens.length; i++){
	aliens[i].show();
	}

	for(var i = 0; i < shots.length; i++){
		shots[i].show();
		shots[i].move();
/*
      for(var j = 0; j < aliens.length; j++)
        if(shots[i].hits(aliens[j])){
          console.log("BOOM");
        }
*/

		}


  if(keyIsDown(RIGHT_ARROW)){
	  ship.move(2);
  }
  else if (keyIsDown(LEFT_ARROW)){
	  ship.move(-2);
  }

}
function keyPressed(){
	if (key === ' ') {
		var shot = new Shot(ship.x, ship.y);
		shots.push(shot);
		console.log("SHOT! AH WE ARE DYING!");
	}
}
