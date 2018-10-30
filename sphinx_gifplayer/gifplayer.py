from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from docutils.parsers.rst import directives


class gifplayer(nodes.General, nodes.Element):
    pass


class GifplayerDirective(SphinxDirective):
    required_arguments = 0
    optional_arguments = 0
    has_content = True

    def run(self):
        node = gifplayer('')
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


gifplayer_controls_html = """
<div id="controller-bar" style="text-align:center;">
    <button id="backward" href="#">|< Step back </button>&nbsp;&nbsp;
    <button id="play" href="#"> Play | Pause </button>&nbsp;&nbsp;
    <button id="forward" href="#"> Step forward >|</button>
</div>
"""

gifplayer_javascript = """
<script type="text/javascript" src="../_static/libgif.js"></script>
<script>
if (window.location.protocol != "file:") {

     var img_elem = $("div.gifplayer").find("img");

     var img_clone = img_elem.clone().appendTo('.section:first');
     img_clone.show();
     var width = img_clone[0].offsetWidth;
     img_clone.remove();

    var gif = new SuperGif({
        gif: img_elem[0],
        max_width: width,
        loop_mode: 'auto',
        auto_play: false,
        draw_while_loading: false,
    });


    gif.load();
    gif.pause();

    $('button#backward').click(function(){
        var total_frames = gif.get_length();
        gif.pause();
        if(gif.get_current_frame() == 0) {
            gif.move_to(total_frames-1);
        } else {
            gif.move_relative(-1);
        }
    })


    $('button#play').click(function(){
        if(gif.get_playing()){
            gif.pause();
        } else {
            gif.play();
        }
    })

    $('button#forward').click(function(){
        gif.pause();
        gif.move_relative(1);
    })
}
</script>
"""


def visit_gifplayer_node(self, node):
    self.body.append(self.starttag(node, 'div', CLASS="gifplayer"))


def depart_gifplayer_node(self, node):
    self.body.append(gifplayer_controls_html)
    self.body.append(gifplayer_javascript)
    self.body.append('</div>\n')


def setup(app):
    directives.register_directive('gifplayer', GifplayerDirective)
    app.add_node(gifplayer, html=(visit_gifplayer_node, depart_gifplayer_node))
