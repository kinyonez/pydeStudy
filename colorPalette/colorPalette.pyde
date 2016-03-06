def setup():
  global img1, mode
  img1 = loadImage("1.png")
  size(800, 600)
  frameRate(1)
  colorMode(HSB)
  noStroke()
  mode = 0

def draw():
  global img1, cColorList, mode
  cSize = 10
  cColorList = []
  # セルの色を配列[cColorList]に格納
  for y in range(height / cSize):
    cY = y * cSize
    for x in range(width / cSize):
      cX = x * cSize
      cColorList.append((
                         hue(img1.get(cX, cY)),
                         saturation(img1.get(cX, cY)),
                         brightness(img1.get(cX, cY))
                         ))
  print len(cColorList)
  print "befote"
  print cColorList[10]

  # 配列[cColorList]を選択したパラメータでソートし配列[cColorSorted]に格納
  if mode % 3 == 0:
    cColorSorted = sorted(cColorList, key = lambda x: x[0])
  elif mode % 3 == 1:
    cColorSorted = sorted(cColorList, key = lambda x: x[1])
  elif mode % 3 == 2:
    cColorSorted = sorted(cColorList, key = lambda x: x[2])

  print mode % 3
  print "after"
  print cColorList[10]
  
  # 配列[cColorSorted]を横書きで順に描画
  i = 0
  for y in range(height / cSize):
    cY = y * cSize
    for x in range(width / cSize):
      cX = x * cSize
      cColor = color(
                     floor(cColorSorted[i][0]), 
                     floor(cColorSorted[i][1]), 
                     floor(cColorSorted[i][2])
                     )
      print cColor
      fill(cColor)
      rect(cX, cY, cSize, cSize)
      i += 1

def mousePressed():
  global cColorList, mode
  mode += 1