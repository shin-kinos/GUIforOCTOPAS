
import os
import os.path # For file exist checking
import webbrowser
import toytree
import toyplot
import toyplot.html
#import toyplot.png

# Create trees plot HTML file 
def render_result_trees(
        input_tree,
        output_tree,
        file_path,
        leaves_label
    ):
    print( '\nRendering trees plot ...' )

    # Check leaves label option
    node_hover_opt = False
    if   ( leaves_label == 'No labels in trees'   ): node_hover_opt = False
    elif ( leaves_label == 'Show labels in trees' ): node_hover_opt = True

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
        nrows            = 2,
        ncols            = 1,
        layout           = 'd',
        edge_type        = 'c',
        tip_labels       = False,
        tip_labels_align = False,
        node_labels      = None,
        node_sizes       = 15,
        node_colors      = 'transparent',
        scalebar         = True,
        node_hover       = node_hover_opt,
        height           = 600,
        width            = 1000
    )
    # Render PNG file (v0.1.3: it is not used anymore !!!)
    #png.render( canvas, file_path )
    #toyplot.browser.show( canvas )

    # Render HTML file
    toyplot.html.render( canvas, file_path )

    print( '=> DONE' )
    return

def show_trees( file_path ):
    print( '\nShowing temp HTML file in browser...' )
    if ( os.path.exists( file_path ) == True ):
        webbrowser.open_new_tab( 'file:///' + file_path )
        print( '=> DONE' )
    else:
        print( 'WARNING : The tempfile \'' + file_path + '\' does not exist!' )
        print( '=> DONE' )
    return