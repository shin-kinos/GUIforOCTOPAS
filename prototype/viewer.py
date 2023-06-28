
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
    tree_list     = toytree.mtree( tree_combined )
    # Create trees plot in HTML format
    canvas, axes, mark = tree_list.draw(
        node_colors  = 'red',
        nrows       = 2,
        ncols       = 1,
        layout      = 'd',
        edge_type   = 'c',
        tip_labels  = False,
        scalebar    = True,
        height      = 600,
        width       = 1000
    )
    # Render HTML file
    toyplot.html.render( canvas, file_path )

    # Convert HTML into PNG
    file_path_png = file_path + '.png'
    png.render( canvas, file_path_png )
    #imgkit.from_file( file_path, file_path_png )

    file_path = 'file:///' + file_path
    webbrowser.open_new_tab( file_path )

    print( '=> DONE' )
    return