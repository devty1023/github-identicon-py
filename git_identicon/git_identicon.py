
import md5
import math
import Image
import ImageDraw

class Git_Identicon(object):
    """
    Git_Identicon creates git style identicon based on string's hex value
    Requries PIL for python
    """

    def __init__(self, string="git_ident", size=126, margin=0.08, background=0xeeeeee) :
        self.string=string                          # string to hash

	# NOTE: size>126, eles math.floor devastates the image
	# resize at the end if necessary
        self.size=size if size>=126 else 126        # size of image
        self.bg=background                          # background color
        self.hash=md5.md5(self.string).hexdigest()  # hash
	self.border=math.floor( self.size*margin )	    # border
        self.square=math.floor( (self.size-(self.border*2)) / 5 )# square width
        self.dec = lambda hex: int(hex, 16)

	# generate pretty color
        self.mix=(255,255,255)
	self.fg=( (self.dec(self.hash[11:13]) + self.mix[0]) / 2, ( self.dec(self.hash[8:10]) + self.mix[0] )/2, (self.dec(self.hash[5:7]) + self.mix[0]) / 2)

        self.draw_image()
	if( size < 126 ):
	  # rezie of image is small
	  self.image.thumbnail((size,)*2, Image.ANTIALIAS)
        #self.image.save("test.png", 'PNG')
	
    def draw_image(self):   
        """
        draw_image(self) -> None
        draws github style identicon
        """

        # begin drawing
        self.image=Image.new('RGB', (self.size,)*2, color=self.bg)
        self.draw=ImageDraw.Draw(self.image)
	border=self.border
        for i in range(15):
            if self.dec(self.hash[i])%2==0:
                if i < 5 :
		    # color mid section
		    x=self.square*2+border
		    y=self.square*i+border
                    self.draw.rectangle([x,y,x+self.square,y+self.square], fill=self.fg)
                elif i < 10:
		    # color 2nd column
		    x=self.square*1+border
		    y=self.square*(i-5)+border
                    self.draw.rectangle([x,y,x+self.square,y+self.square], fill=self.fg)
		    # mirror
		    x=self.square*3+border
                    self.draw.rectangle([x,y,x+self.square,y+self.square], fill=self.fg)
                elif i < 15:
		    # color 1st column
		    x=self.square*0+border
		    y=self.square*(i-10)+border
                    self.draw.rectangle([x,y,x+self.square,y+self.square], fill=self.fg)
		    x=self.square*4+border
                    self.draw.rectangle([x,y,x+self.square,y+self.square], fill=self.fg)
