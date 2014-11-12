import ROOT
ROOT.gROOT.SetBatch(ROOT.kTRUE)

# Set the style of everything
GS = ROOT.gStyle
GS.SetOptStat(0)
GS.SetPadTickX(1)
GS.SetPadTickY(1)
GS.SetFillStyle(ROOT.kWhite)
GS.SetOptTitle(0)
GS.SetFrameBorderMode(ROOT.kWhite)
GS.SetFrameFillColor(ROOT.kWhite)
GS.SetCanvasBorderMode(ROOT.kWhite)
GS.SetCanvasColor(ROOT.kWhite)
GS.SetPadBorderMode(ROOT.kWhite)
GS.SetPadColor(ROOT.kWhite)
GS.SetStatColor(ROOT.kWhite)
GS.SetErrorX(0)

# Tweak some values to save some space and make things look good
GS.SetPadRightMargin(0.05)
GS.SetPadLeftMargin(0.12)
GS.SetPadTopMargin(0.05)

# Canvas size (changing this means retweaking the above!)
cw = 800
ch = 600

# Create colors
class color_object:
    def __init__(self, name, ROOT_color, start, end):
        self.ROOT_color = ROOT_color
        self.name  = name
        self.start = start
        self.end   = end

colors = []
colors.append(color_object('kRed'    , ROOT.kRed    ,-9, 4 ))
colors.append(color_object('kMagenta', ROOT.kMagenta,-9, 4 ))
colors.append(color_object('kBlue'   , ROOT.kBlue   ,-9, 4 ))
colors.append(color_object('kCyan'   , ROOT.kCyan   ,-9, 4 ))
colors.append(color_object('kGreen'  , ROOT.kGreen  ,-9, 4 ))
colors.append(color_object('kYellow' , ROOT.kYellow ,-9, 4 ))
colors.append(color_object(''        , 0            , 0, 0 ))
colors.append(color_object('kPink'   , ROOT.kPink   ,-9, 10))
colors.append(color_object('kViolet' , ROOT.kViolet ,-9, 10))
colors.append(color_object('kAzure'  , ROOT.kAzure  ,-9, 10))
colors.append(color_object('kTeal'   , ROOT.kTeal   ,-9, 10))
colors.append(color_object('kSpring' , ROOT.kSpring ,-9, 10))
colors.append(color_object('kOrange' , ROOT.kOrange ,-9, 10))
colors.append(color_object(''        , 0            , 0, 0 ))
colors.append(color_object('kWhite'  , 0            , 0, 9 ))
colors.append(color_object('kGray'   , ROOT.kGray   , 0, 3 ))
nRow = len(colors)

# Decide how far to go in the +ve and -ve directions in terms of shades
x_lower = -9
x_upper = 11
nCol = x_upper-x_lower

y_lower = 0
y_upper = nRow

# Create a histogram to hold the labels
# This is lazy, but it works well
hBase = ROOT.TH2F('hBase','',nCol,x_lower,x_upper,nRow,y_lower,y_upper)
hBase.GetXaxis().SetTitle('Index')
#hBase.GetXaxis().SetTicks('+-') # Only really used for debugging things
#hBase.GetYaxis().SetTicks('+-') # Only really used for debugging things
hBase.GetXaxis().SetTitleOffset(1.25) # Give some more space for bin labels
hBase.GetXaxis().SetLabelSize(0.05) # About as big as is comfortable given the other tweaks
hBase.GetYaxis().SetLabelSize(0.05) # About as big as is comfortable given the other tweaks
#hBase.GetYaxis().SetTitle('Color') # Remove to save space/reduce clutter

# Set labels on axes
for i in range(0,len(colors)):
    hBase.GetYaxis().SetBinLabel(i+1,colors[i].name)
for bin in range(1,hBase.GetXaxis().GetNbins()+1):
    sign = '' if hBase.GetXaxis().GetBinLowEdge(bin)<0 else '+'
    value = hBase.GetXaxis().GetBinCenter(bin)-0.5
    hBase.GetXaxis().SetBinLabel(bin,'%s%.0f'%(sign,value))

# Now create a box per color
boxes = []
for r in range(0,nRow):
    for c in range(0,nCol):
        base_color = colors[r].ROOT_color
        if colors[r].name=='':
            continue
        index = int(c + x_lower)
        if index < colors[r].start:
            continue
        if index > colors[r].end:
            continue
        x = x_lower+c
        y = y_lower+r
        w = 1
        h = 1
        box = ROOT.TBox(x,y,x+w,y+h)
        color = int(base_color+index)
        box.SetFillColor(color)
        box.SetFillStyle(1001)
        box.SetLineColor(ROOT.kBlack)
        box.SetLineWidth(1)
        boxes.append(box)

# Draw everything and save to file
canvas = ROOT.TCanvas('canvas', '', 0, 0, cw, ch)
hBase.Draw()
for b in boxes:
    b.Draw('l')
canvas.Print('colors.eps')
canvas.Print('colors.png')
