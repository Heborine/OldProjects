function Shot(x, y) {
	this.x = x;
	this.y = y;
	this.r = 4
this.markedForRemoval = false

	this.show= function () {
		fill(255);
		ellipse(this.x, this.y, this.r*2, this.r*2);
	}

	this.move= function(){
		this.y = this.y - 1;

	}

	this.hits = function(alien)	{
	var d = dist(this.x, this.y, alien.x, alien.y);
	if (d < this.r + alien.r) {
		this.markedForRemoval = true;
		alien.markedForRemoval = true;
	} else {
		return false;
	}
}
}
