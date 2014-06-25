#!/usr/bin/python
# coding=utf8

import gtk

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', u'ä', u'ö', u'ü', ' ']

def encrypt(string, x, y):
    string = string.decode("utf8")
    temp = ""
    
    for char in string:
        if char in chars:
            temp += char
        else:
            temp += " "
    string = temp
    
    if len(string) % 2 is not 0:
        string+=" "

    char1 = [i for i in string[0:-1:2].lower()]
    char2 = [i for i in string[1::2].lower()]

    chars_x = [i for i in chars]
    chars_y = [i for i in chars]

    move_x = int(x)
    move_y = int(y)

    for i in xrange(move_x):
        chars_x.insert(0, chars_x.pop())
    for i in xrange(move_y):
        chars_y.insert(0, chars_y.pop())
    
    result = ""
    result += "%03d %03d "%(move_x, move_y)

    for i in xrange(len(char1)):
        result += "%03d "%(chars_x.index(char1[i])+len(chars_x)*(chars_y.index(char2[i]))+len(chars_x)+1)
    
    return result
        
def decrypt(string):
    string = u"".join(string).rstrip(" ").split(' ')
    chars_x = [i for i in chars]

    chars_y = [i for i in chars]

    move_x = int(string[0])
    move_y = int(string[1])

    for i in xrange(move_x):
        chars_x.insert(0, chars_x.pop())
    for i in xrange(move_y):
        chars_y.insert(0, chars_y.pop())

    output = ""
    
    for num in [int(i) for i in string[2:]]:
        output+="%s%s"%(chars_x[(num-len(chars))%len(chars)-1], chars_y[int((num-len(chars)-1)/len(chars))])

    return output

def delete_event(widget, event, data=None):
    return False

def destroy(widget, data=None):
    gtk.main_quit()

def code(widget):
    global textbuffer
    start, end = textbuffer.get_bounds()
    if widget.get_label() == "encode":
        try:
            textbuffer.set_text(encrypt(textbuffer.get_text(start, end),
                spinner_x.get_value_as_int(),
                spinner_y.get_value_as_int()))
        except:
            raise
        widget.set_label("decode")
    else:
        try:
            textbuffer.set_text(decrypt(textbuffer.get_text(start, end)))
        except:
            raise
        widget.set_label("encode")

window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.connect("delete_event", delete_event)
window.connect("destroy", destroy)
window.show()

vbox = gtk.VBox()
window.add(vbox)
vbox.show()

sw = gtk.ScrolledWindow()
sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
textview = gtk.TextView()
textview.set_wrap_mode(gtk.WRAP_WORD)
textbuffer = textview.get_buffer()
sw.add(textview)
sw.show()
textview.show()

vbox.pack_start(sw)

hbox = gtk.HBox()
vbox.pack_start(hbox, False, True, 0)
hbox.show()

button = gtk.Button("encode")
button.connect("clicked", code)
hbox.pack_start(button)
button.show()

adjustment_x = gtk.Adjustment(value=0, lower=0, upper=30, step_incr=1, page_incr=0, page_size=0)
spinner_x = gtk.SpinButton(adjustment_x, 0, 0)
hbox.pack_start(spinner_x)
spinner_x.show()

adjustment_y = gtk.Adjustment(value=0, lower=0, upper=30, step_incr=1, page_incr=0, page_size=0)
spinner_y = gtk.SpinButton(adjustment_y, 0, 0)
hbox.pack_start(spinner_y)
spinner_y.show()

gtk.main()

