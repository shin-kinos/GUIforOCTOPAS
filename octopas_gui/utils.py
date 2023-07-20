
import os
import os.path # For file exist checking
import random
import string
import time

# Input read newick file
def read_newick( file_path ):
    fin = open( file_path, 'r' )
    file_content = fin.readline()
    return file_content

# Check options
def check_options(
    stop_option,
    threshold,
    resolution
):
    #print( stop_option )
    #print( threshold   )
    #print( resolution  )

    if ( stop_option == 'Relative tree length' and threshold.replace( '.', '', 1 ).isdigit() == False ):
        return( 'error', 'Threshold of RTL must be real number.' )

    if ( stop_option == 'Relative tree length' and threshold.replace( '.', '', 1 ).isdigit() == True ):
        if ( float( threshold ) < 0.0 or float( threshold ) > 1.0 ):
            return( 'error', 'Threshold of RTL must be at range of [0, 1].' )

    if ( stop_option == '# of leaves remain' and threshold.isdigit() == False ):
        return( 'error', 'Threshold of remaining leaves number must be integer.' )

    if ( stop_option == '# of leaves remain' and threshold.isdigit() == True ):
        if ( int( threshold ) < 3 ):
            return( 'error', 'Threshold of leaves number must be 3 or more.' )

    if ( resolution.isdigit() == False ):
        return( 'error', 'Resolution must be integer.' )

    if ( int( resolution ) < 1 ):
        return( 'error', 'Resolution must be 1 or more.' )

    return( 'ok', '' )

# Define output leaves file name
# This is to avoid overwritten of same name file
def out_leaves_file_name( dir_name ):
    # Initialise output file name
    file_name = ''
    # Check if same name file exists in directory
    if   ( os.path.exists( dir_name + '/result_leaves.txt' ) == False ): return( 'result_leaves.txt' )
    elif ( os.path.exists( dir_name + '/result_leaves.txt' ) == True  ):
        # Initialise copy number ( result_leaves(n).txt)
        copy_num = 1
        while( True ):
            file_name = 'result_leaves' + '(' + str( copy_num ) + ').txt'
            if ( os.path.exists( dir_name + '/' + file_name ) == False ): break
            copy_num += 1

    return( file_name )

# Define output tree file name
# This is to avoid overwritten of same name file
def out_tree_file_name( dir_name ):
    # Initialise output file name
    file_name = ''
    # Check if same name file exists in directory
    if   ( os.path.exists( dir_name + '/result_tree.newick' ) == False ): return( 'result_tree.newick' )
    elif ( os.path.exists( dir_name + '/result_tree.newick' ) == True  ):
        # Initialise copy number ( result_tree(n).newick )
        copy_num = 1
        while( True ):
            file_name = 'result_tree' + '(' + str( copy_num ) + ').newick'
            if ( os.path.exists( dir_name + '/' + file_name ) == False ): break
            copy_num += 1

    return( file_name )

''' This function is not used anymore !!!
# Define output tree HTML file name
# This is to avoid overwritten of same name file
def out_trees_html_name( dir_name ):
    # Initialise output file name
    file_name = ''
    #print(''.join(random.choices(string.ascii_letters, k=5)))
    # Check if same name file exists in directory
    if   ( os.path.exists( dir_name + '/result_trees_plot.html' ) == False ): return( 'result_trees_plot.html' )
    elif ( os.path.exists( dir_name + '/result_trees_plot.html' ) == True  ):
        # Initialise copy number ( result_trees_plot(n).html )
        copy_num = 1
        while( True ):
            file_name = 'result_trees_plot' + '(' + str( copy_num ) + ').html'
            if ( os.path.exists( dir_name + '/' + file_name ) == False ): break
            copy_num += 1

    return( file_name )
'''

# Define output tree visualisation PNG file name
# Randomised name temporary file is generated
def out_trees_png_path():
    print( '\nGenerating tempfile name ...' )
    # Initialise output file name
    file_name = ''
    file_path = ''
    while( True ):
        random_str = ''.join( random.choices( string.ascii_letters, k = 10 ) )
        file_name  = 'tempfile_' + random_str + '.png'
        file_path  = os.getcwd() + '/' + file_name
        if ( os.path.exists( file_path ) == False ): break

    print( '=> DONE : ' + file_name )
    return( file_path )

# Define output tree visualisation PNG file name
# Randomised name temporary file is generated
def out_trees_html_path():
    print( '\nGenerating temp HTML file name ...' )
    # Initialise output file name
    file_name = ''
    file_path = ''
    while( True ):
        random_str = ''.join( random.choices( string.ascii_letters, k = 10 ) )
        file_name  = 'tempfile_' + random_str + '.html'
        file_path  = os.getcwd() + '/' + file_name
        if ( os.path.exists( file_path ) == False ): break

    print( '=> DONE : ' + file_name )
    return( file_path )

# Remove temp file
def remove_tempfile( file_path ):
    print( '\nRemoving temp HTML file ...' )
    if ( os.path.exists( file_path ) == True ):
        # just wait 2 secs to avoid removing
        # HTML file before opening it.
        time.sleep( 1 )
        os.remove( file_path )
        print( '=> DONE' )
    else:
        print( 'WARNING : The tempfile \'' + file_path + '\' does not exist!' )
        print( '=> DONE' )

    return

# Tooltip messages
help_input      = 'The input file must be Newick format.'
help_example    = 'This example tree is composed of\nhighly redundant 300 leaves of\nhemoglobin subunit alpha\nAA sequences obtained from\nUniProt KB (swissprot).'
help_stopoption = '\'# of leaves remain\' represents\na stop option of how many\nleaves you would like to keep.\n\'Relative tree length\' is a\nthreshold by calculating total\nbranch length of pruned tree\ndevided by total branch length\nof original tree.'
help_threshold  = 'IMPORTANT: If the stop option\nis \'# of leaves remain\', this value\nmust be 3 or more integer\nnumber. If \'Relative tree length\',\nthis value must be real number\nat the range of [0, 1].'
help_resolution = 'This value must be 1 or more\ninteger number. e.g. If the\nresolution is 5, the top 5\nredundant leaves are pruned\nin one iteration.'
help_viewer     = 'Quick and simple view of the\nresult trees. NOTE that the tree\nat the top place is the original\ninput tree, and one on the\nbottom is the result pruned tree.'
help_treelable  = 'Whether or not information in\neach leaf is shown when hover\nover. If \'Show labels in trees\',\nthe generated HTML on browser\nwill have a functionality\nshowing some information\nabout leaves when the user hover\nover them. NOTE: the rendering\nof them might take long time\nwhen the input file is large (e.g.,\nmore than 1000 leaves).'
