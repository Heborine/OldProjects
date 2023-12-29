function Ship(){
this.x = width/2;
this.y = height-30;

this.show = function(){
fill(255);
rectMode(CENTER);
rect(this.x, this.y, 20,40);
}

this.move = function(dir){
	this.x += dir;
	if(this.x > width){
		this.x = 0;
	}
	if(this.x < 0){
		this.x = width;
	}
}
}