# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cassava']

package_data = \
{'': ['*']}

install_requires = \
['blessed>=1.18.1,<2.0.0', 'matplotlib>=3.4.3,<4.0.0']

setup_kwargs = {
    'name': 'cassava-csv',
    'version': '0.1.0',
    'description': 'Cassava is a package for reading, plotting and quality-checking CSV files.',
    'long_description': '# cassava\n\nCassava is a package for reading, plotting and quality-checking CSV files.  It\'s primary purpose is for giving a quick, first assessment of a CSV file, highlighting common quality issues such as wholly empty columns or rows, differing column counts and basic outlier detection.  The package can be integrated as part of a larger workflow, or used directly from the command line with a simple but functional command line interface (CLI).\n\n## Install\n\nThe package can be installed from PyPI (note the package distribution name):\n\n```bash\n$ pip install cassava-csv\n```\n\n## From the command line\n\nThe cassava CLI runs in a number of modes.  The main commands are `plot`, to visually inspect a file, and `print`, to print its findings to `stdout`.  For each of these commands, there are two subcommands; `qc` for producing a QC plot or report, and `stats` for producing a summary statistics plot or report.  There are then many options to specify how to read and process the CSV file, e.g., whether it has a header row, which column to use for the x-axis in the plot, which columns to use for the y-axis in the plot etc.\n\n### Synopsis\n\nThe general usage is to call the cassava package main, followed by any options, then the command (one of `plot`, `print`), a subcommand (one of `qc`, `stats`) and finally the input CSV file.  Note that the subcommand is optional and if not supplied, will default to `qc`.\n\n```bash\n$ python -m cassava [opts] command [subcommand] input.csv\n```\n\nSpecifying the `--help` option, will print the CLI usage and quit.  To get help on a given command, specify the `--help` option after that command.  For example:\n\n```bash\n$ python -m cassava plot --help \n```\n\nNote that the options are global to all modes (commands and subcommands), even when some only really make sense for a given mode.  This is by design, and to make for an uncomplicated CLI, which lends itself well to just pressing "up arrow" in the shell and using the same options but in a different mode.\n\n### Options\n\n```\n  -h, --help            show this help message and exit\n  -H HEADER_ROW, --header-row HEADER_ROW\n                        row containing the header\n  -i FIRST_DATA_ROW, --first-data-row FIRST_DATA_ROW\n                        first row containing data to plot\n  -x XCOL, --x-column XCOL\n                        column containing values for the x-axis\n  -y YCOL, --y-column YCOL\n                        column containing values for the y-axis (specify\n                        multiple columns separated by commas to plot multiple\n                        curves on y-axis)\n  -d, --x-as-datetime   treat the x-axis values as datetimes\n  -f DATETIME_FORMAT, --datetime-format DATETIME_FORMAT\n                        datetime format specification\n  -l DELIMITER, --delimiter DELIMITER\n                        alternative delimiter\n  -s, --skip-initial-space\n                        ignore whitespace immediately following the delimiter\n  -F, --forgive         be forgiving when parsing numeric data\n  -N NCOLS, --plot-in-n-columns NCOLS\n                        number of columns for a multi-plot grid\n  -k K, --tukey-fence-factor K\n                        factor to multiply IQR by in Tukey\'s rule\n  -O, --hide-outliers   don\'t show outliers on stats plots\n  -v, --verbose         emit verbose messages\n```\n\n### Examples\n\nGiven the following CSV file:\n\n```\nDatetime,Temperature,Relative_Humidity,Sea_Level_Pressure,Wind_Speed,,,\n1999-12-20T00:00:00,-10,40,990,,,,\n1999-12-21T00:00:00,-11,51,971,,,,\n1999-12-22T00:00:00,-10,62,952,17,,,\n1999-12-23T00:00:00,-10,56,956,,,,\n1999-12-24T00:00:00,-12,78,,,,,\n1999-12-25T00:00:00,-11,77,995,,,,\n1999-12-26T00:00:00,-11,70,986,,,,\n1999-12-27T00:00:00,-12,47,966,22,,,\n1999-12-28T00:00:00,-11,48,990,230,,,\n1999-12-29T00:00:00,-11,57,967,25,,,\n,,,,,,,\n,,,,,,,\n,,,,,,,\n,,,,,\n,,,,,,,,,,,\n```\n\nwe can see a number of issues.  It\'s likely that this was exported from a spreadsheet, as it has a number of trailing empty columns, and trailing empty rows.  In addition, there\'s been some subsequent "finger trouble", as the last two empty rows have differing column counts.  There are wholly empty columns, as well as some sparse, but not wholly empty columns, and at least one highly probable outlier.\n\nOften a quick plot will tell us a lot about our data, so let\'s try that.  If our CSV file contained only numeric columns, with no header, then we could simply do:\n\n```bash\n$ python -m cassava plot data.csv\n\n...\n\nValueError: could not convert string to float: \'Datetime\'\n```\n\nhowever in this case, the default y-axis column (0) contains ISO datetime strings, and the first row is a header row, so cassava will raise the above exception.\n\nAt this point, we could replace the `plot` command with `print`, and get some useful QC information about the file, as the `print` command doesn\'t need to interpret the data as much as the `plot` command does.\n\nA key feature of cassava is that you can run it in "forgive" mode (`-F`), where it will simply replace any invalid numeric values with a placeholder value (the default is NaN).  By default the forgive mode is `False`, otherwise it would mask quality issues with the data, and so defeat the central point of cassava!  However, in cases where we just want to get a first look at the data, the forgive mode is invaluable.  So let\'s do that:\n\n```bash\n$ python -m cassava -F plot data.csv\n```\n\nThis produces a plot, but it\'s empty!  This is because the default y-axis column contains datetime strings, and so the forgive mode has skipped over all of them.  Let\'s specify the y-axis data (`-y`) as column 1:\n\n```bash\n$ python -m cassava -F -y 1 plot data.csv\nNo handles with labels found to put in legend.\n```\n\nThat works, and produces a line plot of the `Temperature` data.  This is a minimal working command line for plotting this file, but we can do better!\n\nLet\'s provide a few more options for processing.  First we can address the notification that `matplotlib` emitted about no labels for the legend.  We can tell cassava that the first row (row 0 - all cassava coordinates have origin zero) is a header row (`-H 0`) and the first data row is the next row (`-i 1`).  Having these as two separate options gives us flexibility for cases where the CSV file may have a complex structured header section.  Furthermore, we note that this is a timeseries, so we can provide options to cassava so that it can treat it as such.  We specify the x-axis data as column 0 (`-x 0`), and tell cassava to treat the x-axis as a datetime column (`-d`).  The datetime format is ISO 8601, which is the cassava default, so we don\'t need to specify the datetime format.  Trying this also raises an exception:\n\n```bash\n$ python -m cassava -H 0 -i 1 -x 0 -d -y 1 plot qc data.csv\n\n...\n\nValueError: Failed to convert x-column at row 11 to datetime: [\'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\']\n```\n\nThis is valuable QC information, as it tells us exactly the row that failed to parse as a datetime.  Particularly useful if the file is large.  At this point we could address the issue directly, by editing the CSV file accordingly (in this example, by removing the empty trailing rows), or just run cassava without specifying the x-axis data (cassava then defaults to integer indices).  Let\'s do the latter:\n\n```bash\n$ python -m cassava -H 0 -i 1 -y 1 plot qc data.csv\n\n...\n\nValueError: could not convert string to float: \'\' \n```\n\nMore valuable QC information!  The empty rows at the bottom of the file cause this exception.  Let\'s reintroduce the forgive option.  This allows us to get on with evaluating the data, but of course eventually, we will remove those empty rows.\n\n```bash\n$ python -m cassava -H 0 -i 1 -y 1 -F plot qc data.csv\n```\n\nThis gives us a nice working command line.  Now let\'s plot all the numeric columns.  We can specify multiple columns for the y-axis by giving a comma-separated list:\n\n```bash\n$ python -m cassava -H 0 -i 1 -y 1,2,3,4 -F plot qc data.csv\n```\n\nThis works, but as the `Sea_Level_Pressure` values are far greater than the other columns, it\'s not easy to pick out the detail.  We could drop the `Sea_Level_Pressure` column from the y-axis list (`-y 1,2,4`).  This is an improvement, but the outlier in `Wind_Speed` is now causing problems.  In cases where your data are of greatly differing scales, it\'s better to plot multiple curves on separate plots.  This can be achieved using the `-N NCOLS` option, which tells cassava to plot a grid of NCOLS-wide plots:\n\n```bash\n$ python -m cassava -H 0 -i 1 -y 1,2,3,4 -F -N 2 plot qc data.csv\n```\n\nThis plots a 2x2 grid of plots, with each variable in its own plot, with a suitably-scaled y-axis.\n\nFor any of the working command lines above, we could replace the `qc` subcommand with the `stats` subcommand, to get summary statistics plots for the specified y-columns.  Let\'s do that for the last command line.  The first thing to note, is that the `-N 2` option is not required for stats plots.  However, as noted above, it doesn\'t hurt to leave it there and thus allows for rapid tweak/repeat cycles:\n\n```bash\n$ python -m cassava -H 0 -i 1 -y 1,2,3,4 -F -N 2 plot stats data.csv\n```\n\nThis produces three plots for each specified y-column: a density plot of the distribution of the data, a line plot of the data including bounds to highlight potential outliers, and a boxplot of the data.  In this example, the outlier in the `Wind_Speed` is clearly identified.  If an outlier is so large that it dominates the remaining data, then we can instruct cassava to not show outliers (`-O`), thereby revealing the detail:\n\n```bash\n$ python -m cassava -H 0 -i 1 -y 1,2,3,4 -F -N 2 -O plot stats data.csv\n```\n\nSimilarly, we can replace the `plot` command with the `print` command.  Let\'s do that (again, no need to remove extraneous options):\n\n```bash\n$ python -m cassava -H 0 -i 1 -y 1,2,3,4 -F -N 2 -O print qc data.csv \nColumn counts:\n    first row 1: ncols = 8\n    row 14: ncols = 6\n    row 15: ncols = 12\nRow counts:\n    total rows = 16, data rows = 15\nEmpty columns:\n    column 5 is empty\n    column 6 is empty\n    column 7 is empty\nEmpty rows:\n    row 11 is empty\n    row 12 is empty\n    row 13 is empty\n    row 14 is empty\n    row 15 is empty\n```\n\nwhich produces the above QC report.  The output is colour-coded using a traffic light system, thereby highlighting quality issues.  For the `Column counts` section, only those rows which have differing column counts to the first data row are listed, so ideally in good data, you would only see the column count of the first data row.  Running the above in verbose mode (`-v`) would list all column counts, irrespective of whether they agree with the first data row or not.\n\nWe can also print summary statistics for the specified columns, and list any cells that contain suspected outlier values:\n\n```bash\n$ python -m cassava -H 0 -i 1 -y 1,2,3,4 -F -N 2 -O print stats data.csv \nColumn stats:\n    column min     mean    max     q1      median  q3      std \n    1      -12     -11     -10     -11     -11     -10     0.7 \n    2      40      59      78      49      56      68      12  \n    3      9.5e+02 9.7e+02 1e+03   9.7e+02 9.7e+02 9.9e+02 15  \n    4      17      74      2.3e+02 21      24      76      90  \nColumn outliers (1.5 * IQR):\n    column,row value   \n    4,9        2.3e+02 \n```\n\n## Using the package\n\nTo use cassava in your own code, setup a configuration `dict`, and then call the required methods from within the `Cassava` context manager:\n\n```python\nfrom cassava import Cassava\n\nfilename = \'data.csv\'\nconf = Cassava.DEFAULTS.copy()\nopts = {\n    \'header_row\': 0,\n    \'first_data_row\': 1,\n    \'ycol\': [1,2,3,4],\n    \'forgive\': True\n}\nconf.update(opts)\n\nwith Cassava(path=filename, conf=conf) as f:\n    f.read()\n    f.plot()\n```\n\n### Configuration dict\n\nAs can be seen above, cassava requires a fully-specified configuration `dict`, so the easiest way to ensure this is to take a copy of the `Cassava` class `DEFAULTS dict`, and then override any specific configuration items.  The default configuration `dict` is:\n\n```python\n    DEFAULTS = {\n        \'header_row\': None,\n        \'first_data_row\': 0,\n        \'xcol\': None,\n        \'ycol\': [0],\n        \'x_as_datetime\': False,\n        \'datetime_format\': \'%Y-%m-%dT%H:%M:%S\',\n        \'delimiter\': \',\',\n        \'skip_initial_space\': False,\n        \'forgive\': False,\n        \'verbose\': False\n    }\n```\n\n* header_row: Integer row index of the input file\'s header\n* first_data_row: Integer row index of the input file\'s first data row\n* xcol: Integer column index from the input file for the plot x-axis\n* ycol: Integer column index `list` from the input file for the plot y-axis\n* x_as_datetime: Consider the x-axis data as datetime strings\n* datetime_format: `datetime.datetime.strptime()` format specification\n* delimiter: Column delimiter character\n* skip_initial_space: Skip any spaces following the delimiter character\n* forgive: Forgive mode. Replace invalid numeric values with placeholder (NaN)\n* verbose: Print extra messages in `print` mode methods\n\nNote that all cassava column/row coordinates have origin zero.\n\n#### Persist custom default configuration for a session\n\nA feature of the `DEFAULTS dict` is that, because it\'s a class variable (rather than an instance variable), you can set per `import` session defaults for all instances by directly updating `DEFAULTS`:\n\n```python\nfrom cassava import Cassava\n\nfilenames = [\'data1.csv\',\'data2.csv\']\nopts = {\n    \'header_row\': 0,\n    \'first_data_row\': 1\n}\nCassava.DEFAULTS.update(opts)\n\nfor filename in filenames:\n    with Cassava(path=filename) as f:\n        f.read()\n        f.plot()\n```\n\nNote that if no configuration `dict` is passed via the `conf` kwarg, then cassava uses `DEFAULTS` instead.\n\n### The cassava object\n\nThe `Cassava` object has the following instance variables:\n\n```python\n        self.path = path\n        self.conf = conf or self.DEFAULTS\n        self.fp = None\n        self.header_row = []\n        self.rows = []\n```\n\n`path` and `conf` are the input file path `str` and the configuration `dict` that are (optionally) passed to the constructor, as shown in the above examples.  `fp` is the file pointer for the input file.  `header_row` (a `list`) holds the (optional) header row, parsed from the input data, and `rows` (a `list` of `list`s) contains the data rows parsed from the input data.\n\n### Reading input data\n\nThe easiest way to get data into cassava, is by using it as a context manager:\n\n```python\nwith Cassava(path=filename, conf=conf) as f:\n    f.read()\n    f.plot_stats()\n```\n\nhowever, you can use the `open/close` methods directly, should you wish:\n\n```python\nc = Cassava(conf=conf)\nc.open(path=filename)\nc.read()\nc.print_qc()\nc.close()\n```\n\nAs noted in the previous section, the `header_row` and `rows` attributes hold the header row and data rows parsed from the input data.  Hence you could also directly set `rows` (and optionally `header_row`), rather than reading them from a file using the `read` method, and still be able to make use of the methods that cassava provides.\n\n#### Reading input data with different delimiters\n\nAlthough by default, cassava is setup to read CSV data, it can actually read any similarly-delimited tabular data.  This is controlled by the `delimiter` configuration item.  For instance a space (`conf[\'delimiter\'] = \' \'`) or a tab (`conf[\'delimiter\'] = \'\\t\'`).  Note that if the columns are separated by multiple spaces (e.g. a fixed width format), then setting `conf[\'skip_initial_space\'] = True` will consume all spaces between the columns.\n\n### Analysing the data\n\nOnce we have the data in cassava, we can produce quick-look plots, generate QC reports and compute summary statistics.\n\n#### Plot the data\n\nTo give an initial exploratory look at the data and assess any QC issues, we can simply plot our dependent variables (our `ycol` columns) by calling `plot()`:\n\n```python\n    f.conf[\'ycol\'] = [1,2,3,4]\n    f.plot()\n```\n\nOur input file may contain an independent variable (e.g. datetime) which we can use for our `xcol` column:\n\n```python\n    f.conf[\'xcol\'] = 0\n    f.conf[\'ycol\'] = [1,2,3,4]\n    f.plot()\n```\n\nIf our dependent variables contain data with differing scales, we can choose to plot them as separate subplots, rather than all on a single plot with a shared y-axis.  We do this by providing a `layout` tuple specifying an `m` rows by `n` columns plot grid (where `m * n > 1`):\n\n```python\n    f.conf[\'ycol\'] = [1,2,3,4]\n    f.plot(layout=(2,2))\n```\n\nOften we don\'t care how many rows the plot grid requires, rather just how many columns wide the grid should be, so we can use the `compute_multi_plot_layout` method to compute our `layout` for us, given our desired number of columns:\n\n```python\n    f.conf[\'ycol\'] = [1,2,3,4]\n    f.plot(layout=f.compute_multi_plot_layout(2))\n```\n\nwhich will produce a 2x2 plot grid.\n\nTo allow some customisation of the plot, we can use the `opts` kwarg.  This takes a `dict`, and can contain any plot kwargs accepted by `matplotlib`:\n\n```python\n    f.plot(opts={\'lw\': 4, \'c\': \'green\', \'ls\': \'--\'})\n```\n\nIn addition, we can defer the showing of the plot via the `show` kwarg.  This allows us to do further customisation of the plot before showing it.  Note that to do this, we have to `import matplotlib` and call `show()` ourselves:\n\n```python\nimport matplotlib.pyplot as plt\n\n    fig, axs = f.plot(show=False)\n    fig.suptitle(f\'Meteorological Data - {filename}\')\n    plt.show()\n```\n\n#### Plot summary statistics for the data\n\nPlotting summary statistics is straightforward:\n\n```python\n    f.conf[\'ycol\'] = [1,2,3,4]\n    f.plot_stats()\n```\n\nThis produces three plots for each specified y-column: a density plot of the distribution of the data, a line plot of the data including bounds to highlight potential outliers, and a boxplot of the data.\n\nNote that the bounds in the line plot, and the whiskers in the boxplot, are scaled according to Tukey\'s rule and are 1.5 * IQR above/below the IQR.  We can change this scale factor via the `k` kwarg:\n\n```python\n    f.plot_stats(k=2.5)\n```\n\nIf we have outliers that are so large that they dominate the remaining data, then we can choose to omit them, thereby revealing the detail:\n\n```python\n    f.plot_stats(showfliers=False)\n```\n\nBy default, the number of bins to use for the density plot is automatically calculated by `matplotlib`.  We can specify these explicitly via the `bins` kwarg, which takes any form supported by `matplotlib.pyplot.hist`:\n\n```python\n    f.plot_stats(bins=10)\n```\n\n#### Print a QC report of the data\n\nTo print a QC report of the data to `stdout`, we can do:\n\n```python\nfilename = \'data.csv\'\n\nwith Cassava(path=filename) as f:\n    f.read()\n    f.print_qc()\n```\n\nwhich outputs the following (using our example data from above):\n\n```bash\nColumn counts:\n    first row 0: ncols = 8\n    row 14: ncols = 6\n    row 15: ncols = 12\nRow counts:\n    total rows = 16, data rows = 16\nEmpty columns:\n    column 5 is empty\n    column 6 is empty\n    column 7 is empty\nEmpty rows:\n    row 11 is empty\n    row 12 is empty\n    row 13 is empty\n    row 14 is empty\n    row 15 is empty\n```\n\nNote that this really requires no configuration, but assumes that our input file has no header row (and so `total rows` == `data rows`), or more generally, that the data begin on the first row (row 0).  If the file does contain a header row, or an extended header section, then we should specify the first data row index for completeness, and so generate a more accurate report:\n\n```python\n    f.conf[\'first_data_row\'] = 1\n    f.print_qc()\n```\n\nThe `print_qc` method is a wrapper around the methods that produce the different output sections in the above output.  Of course, we can call these directly to produce a custom report.  For example:\n\n```python\n    f.print_column_counts()\n    f.print_empty_columns()\n```\n\n#### Print a summary statistics report of the data\n\nHere we require a little more configuration than for a QC report.  We need to specify those columns that we wish to compute summary statistics for, and, taking our example data above, we\'d need to run cassava in forgive mode to skip over our trailing empty rows:\n\n\n```python\n    f.conf[\'first_data_row\'] = 1\n    f.conf[\'ycol\'] = [1,4]\n    f.conf[\'forgive\'] = True\n    f.print_stats()\n```\n\nwhich outputs the following (again using our example data from above):\n\n```bash\nColumn stats:\n    column min mean max     q1  median q3  std \n    1      -12 -11  -10     -11 -11    -10 0.7 \n    4      17  74   2.3e+02 21  24     76  90  \nColumn outliers (1.5 * IQR):\n    column,row value   \n    4,9        2.3e+02 \n```\n\nHere we can see that cassava has identified the value in column 4 (`Wind_Speed`) and row 9 as an outlier, according to Tukey\'s rule.\n\n#### Access the underlying QC and summary statistics data\n\nProducing the plots and printing the reports is fine, but for tighter integration, we can access the underlying `message dict` that encapsulates the QC and statistics information.\n\n##### Message dict\n\nThe general form of the `message dict` is:\n\n```python\nmsg = {\n    \'x\': x_coordinate,\n    \'y\': y_coordinate,\n    \'data\': data_dict,\n    \'status\': status_code\n}\n```\n\n* x: Integer column index of the input data (`None` indicates all columns)\n* y: Integer row index of the input data (`None` indicates all rows)\n* data: A `dict` of the output, specific to each method\n* status: One of the possible status constants from `class CassavaStatus`\n\nNote that all cassava column/row coordinates have origin zero.\n\nFor example, the `check_column_counts` method calculates the column count of each row in the input data.  In particular, it calculates and holds the column count of the configured first data row, and then compares the column counts of all subsequent rows to that of the first, and flags up if they differ.  As this is a per-row check, the x-coordinate is `None` because it refers to all columns for that row.  The column count for the first data row will always have `status = CassavaStatus.ok`:\n\n```python\nmsg = {\n    \'x\': None,\n    \'y\': y,\n    \'data\': {\'is_first_row\': True, \'ncols\': len(row)},\n    \'status\': CassavaStatus.ok\n}\n```\n\nSubsequent rows will have `is_first_row = False`, and `status = CassavaStatus.ok` if their column counts agree with that of the first data row, otherwise they will have `status = CassavaStatus.error`.  (It is the `status` attribute that is used for colour-coding the output in the print functions.)\n\nThe following describe the `message[\'data\'] dict` for each method:\n\n* check_column_counts: {\'is_first_row\': Boolean, \'ncols\': Integer column count}\n* check_empty_columns: {\'is_empty\': Boolean}\n* check_empty_rows: {\'is_empty\': Boolean}\n* compute_column_stats: {\'min\': Minimum, \'mean\': Mean, \'max\': Maximum, \'q1\': Quartile1, \'median\': Quartile2, \'q3\': Quartile3, \'std\': Standard deviation}\n* check_column_outliers_iqr: {\'value\': Cell value}\n\n##### Examples\n\nAs an example, say we wanted to compute the percentage of empty columns and rows in our example file.  We could do:\n\n```python\nfrom cassava import Cassava\n\nfilename = \'data.csv\'\n\nwith Cassava(path=filename) as f:\n    f.read()\n    ncols = len(f.rows[f.conf[\'first_data_row\']])\n    # Uncomment to only consider data rows, rather than total rows\n    # f.conf[\'first_data_row\'] = 1\n    # nrows = len(f.rows) - f.conf[\'first_data_row\']\n    nrows = len(f.rows)\n    empty_ncols = 0\n    empty_nrows = 0\n\n    for msg in f.check_empty_columns():\n        if msg[\'data\'][\'is_empty\']:\n            empty_ncols += 1\n\n    for msg in f.check_empty_rows():\n        if msg[\'data\'][\'is_empty\']:\n            empty_nrows += 1\n\n    print(f\'Empty cols = {empty_ncols / ncols * 100:0.2f}%\')\n    print(f\'Empty rows = {empty_nrows / nrows * 100:0.2f}%\')\n```\n\nTo print the mean of each configured column, we could do:\n\n```python\nfilename = \'data.csv\'\nconf = Cassava.DEFAULTS.copy()\nopts = {\n    \'header_row\': 0,\n    \'first_data_row\': 1,\n    \'ycol\': [1,2,3,4],\n    \'forgive\': True\n}\nconf.update(opts)\n\nwith Cassava(path=filename, conf=conf) as f:\n    f.read()\n    labels = f.get_column_labels_from_header(f.conf[\'ycol\'])\n\n    for msg, label in zip(f.compute_column_stats(), labels):\n        print(f\'{label} mean = {msg["data"]["mean"]:0.2f}\')\n```\n\n',
    'author': 'Paul Breen',
    'author_email': 'pbree@bas.ac.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/paul-breen/cassava',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
