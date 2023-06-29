
import toytree
import toyplot
import webbrowser
import os
import imgkit
from toyplot import png

# Create trees plot HTML file 
def plot_result_trees( input_tree, output_tree, file_path ):
    print( '\nCreating a trees plot ...' )

    # Create multiple tree list for 'toyplot'
    original_tree = input_tree
    pruned_tree   = output_tree

    # Remove blank lines if contained in advance
    original_tree = original_tree.replace( '\n', '' )
    pruned_tree   = pruned_tree.replace(   '\n', '' )

    # Combine 2 trees by blank line
    tree_combined = original_tree + '\n' + pruned_tree
    #print( tree_combined )

    # Make it into mtree object
    tree_list = toytree.mtree( tree_combined )

    # Create trees plot in HTML format
    canvas, axes, mark = tree_list.draw(
        nrows       = 2,
        ncols       = 1,
        layout      = 'd',
        edge_type   = 'c',
        tip_labels  = False,
        scalebar    = True,
        height      = 450,
        width       = 800
    )
    # Render HTML file (v.0.1.2: it is not used anymore!)
    #toyplot.html.render( canvas, file_path )

    # Render PNG file
    png.render( canvas, file_path )

    print( '=> DONE' )
    return