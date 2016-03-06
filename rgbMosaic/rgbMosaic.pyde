def setup():
  global img1
  img1 = loadImage("1.png")
  size(800, 600)
  colorMode(RGB)
  noStroke()
  frameRate(5)

def draw():
  global img1
  background(0)
  cSize = mouseX/10 + 2
  xSize = cSize + cSize*cos(PI/3)
  ySize = 2 * cSize*sin(PI/3)
  for x in range(floor(width / xSize) + 1):
    cX = x * xSize
    for y in range(floor(height / ySize) + 2):
      cY = y * ySize
      if x % 2 == 1:
        cY -= ySize / 2
      cColor = img1.get(floor(cX), floor(cY + cSize*(2/3 * cos(PI/6))))
      rSize = map(red(cColor), 0, 255, 0, 2 * cSize * sin(PI/3))
      gSize = map(green(cColor), 0, 255, 0, 2 * cSize * sin(PI/3))
      bSize = map(blue(cColor), 0, 255, 0, 2 * cSize * sin(PI/3))
      fill(255, 0, 0, 100)
      ellipse(cX, cY, rSize, rSize)
      fill(0, 255, 0, 100)
      ellipse(cX + (cSize * sin(PI/6)), cY + (cSize * cos(PI/6)), gSize, gSize)
      fill(0, 0, 255, 100)
      ellipse(cX - (cSize * sin(PI/6)), cY + (cSize * cos(PI/6)), bSize, bSize)