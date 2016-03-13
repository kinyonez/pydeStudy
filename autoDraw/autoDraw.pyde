def setup():
  global img1, X, Y, randWidth
  img1 = loadImage("1.png")
  size(800, 600)
  frameRate(300)
  X = width / 2
  Y = height / 2
  randWidth = 100

def draw():
  global img1, X, Y, randWidth
  pX = X
  pY = Y
  addX = random(-randWidth, randWidth)
  addY = random(-randWidth, randWidth)
  X = pX + addX
  Y = pY + addY
  if X > width:
    X = 0
    pX = 0
  if X < 0:
    X = width
    pX = width
  if Y > height:
    Y = 0
    pY = 0
  if Y < 0:
    Y = height
    pY = height
  cX = floor((X+pX) / 2)
  cY = floor((Y+pY) / 2)
  lineColor = img1.get(cX, cY)
  lineWeight = map(dist(pX, pY, X, Y), 0, dist(0, 0, 100, 100), 1, 30)
  stroke(lineColor)
  strokeWeight(lineWeight)
  line(pX, pY, X, Y)
  textSize(20)
  fill(0)
  noStroke()
  rect(10, 3, floor(textWidth("XXX")), 20)
  fill(255)
  text(randWidth, 10, 20)

def mousePressed():
  global randWidth
  if randWidth <= 5:
    randWidth = 100
  randWidth = randWidth / 2