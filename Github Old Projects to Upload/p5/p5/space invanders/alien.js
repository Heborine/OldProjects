function Alien(x,y)
{
	this.x = x;
this.y = y;
this.r = 30;
this.markedForRemoval = false

this.show = function()
{
	fill(0,255,32);
	ellipseMode(CENTER);
	ellipse(this.x, this.y, this.r*2,this.r*2);
}
this.move = function (dir)
{
	this.x += dir;
	if(this.x > width){
		this.x = 0;
	}
}
this.destruct = function(){
	this.markedForRemoval = true;
}

}
