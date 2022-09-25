{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "998f7219",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'kiwisolver._cext'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_28012/1258372826.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mmatplotlib\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpyplot\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[0mget_ipython\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrun_line_magic\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'matplotlib'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'inline'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\user\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\matplotlib\\__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m    155\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    156\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 157\u001b[1;33m \u001b[0m_check_versions\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    158\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    159\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\user\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\matplotlib\\__init__.py\u001b[0m in \u001b[0;36m_check_versions\u001b[1;34m()\u001b[0m\n\u001b[0;32m    149\u001b[0m             \u001b[1;33m(\u001b[0m\u001b[1;34m\"pyparsing\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"2.2.1\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    150\u001b[0m     ]:\n\u001b[1;32m--> 151\u001b[1;33m         \u001b[0mmodule\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mimportlib\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mimport_module\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmodname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    152\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mLooseVersion\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmodule\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__version__\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m<\u001b[0m \u001b[0mminver\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    153\u001b[0m             raise ImportError(\"Matplotlib requires {}>={}; you have {}\"\n",
      "\u001b[1;32mc:\\users\\user\\appdata\\local\\programs\\python\\python37\\lib\\importlib\\__init__.py\u001b[0m in \u001b[0;36mimport_module\u001b[1;34m(name, package)\u001b[0m\n\u001b[0;32m    125\u001b[0m                 \u001b[1;32mbreak\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    126\u001b[0m             \u001b[0mlevel\u001b[0m \u001b[1;33m+=\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 127\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0m_bootstrap\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_gcd_import\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mlevel\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpackage\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlevel\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    128\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    129\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\user\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\kiwisolver\\__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;31m# The full license is in the file LICENSE, distributed with this software.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;31m# --------------------------------------------------------------------------------------\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 8\u001b[1;33m from ._cext import (\n\u001b[0m\u001b[0;32m      9\u001b[0m     \u001b[0mBadRequiredStrength\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m     \u001b[0mConstraint\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'kiwisolver._cext'"
     ]
    }
   ],
   "source": [
    "import scipy.stats\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "42e6cd1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def drawPowerLawGraph(csv_file_name):\n",
    "    dataFrame = pd.read_csv(csv_file_name)\n",
    "    dataFrame.drop(dataFrame.filter(regex=\"Unname\"),axis=1, inplace=True)\n",
    "    final_df = dataFrame.sort_values(by=['inDegree'],ascending=True)\n",
    "    x=final_df['inDegree']\n",
    "    y=final_df['count']\n",
    "    plt.plot(x,y)\n",
    "    plt.xlabel('degree')\n",
    "    plt.ylabel('count')\n",
    "    plt.title('Graph of csv'+csv_file_name)\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "6e9cb06c",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'amazon.graph.large.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_28012/3562307139.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdrawPowerLawGraph\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'amazon.graph.large.csv'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mdrawPowerLawGraph\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'amazon.graph.small.csv'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mdrawPowerLawGraph\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'youtube.graph.large.csv'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mdrawPowerLawGraph\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'youtube.graph.small.csv'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mdrawPowerLawGraph\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'dblp.graph.large.csv'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_28012/505128449.py\u001b[0m in \u001b[0;36mdrawPowerLawGraph\u001b[1;34m(csv_file_name)\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mdrawPowerLawGraph\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcsv_file_name\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m     \u001b[0mdataFrame\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcsv_file_name\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m     \u001b[0mdataFrame\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdrop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdataFrame\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfilter\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mregex\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"Unname\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0maxis\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0minplace\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mfinal_df\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdataFrame\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msort_values\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mby\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'inDegree'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mascending\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[0mx\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mfinal_df\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'inDegree'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\user\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36mread_csv\u001b[1;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, dialect, error_bad_lines, warn_bad_lines, delim_whitespace, low_memory, memory_map, float_precision)\u001b[0m\n\u001b[0;32m    686\u001b[0m     )\n\u001b[0;32m    687\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 688\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0m_read\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    689\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    690\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\user\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m_read\u001b[1;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[0;32m    452\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    453\u001b[0m     \u001b[1;31m# Create the parser.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 454\u001b[1;33m     \u001b[0mparser\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mTextFileReader\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfp_or_buf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    455\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    456\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mchunksize\u001b[0m \u001b[1;32mor\u001b[0m \u001b[0miterator\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\user\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[0;32m    946\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"has_index_names\"\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mkwds\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"has_index_names\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    947\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 948\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_make_engine\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mengine\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    949\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    950\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mclose\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\user\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m_make_engine\u001b[1;34m(self, engine)\u001b[0m\n\u001b[0;32m   1178\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_make_engine\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mengine\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"c\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1179\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mengine\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m\"c\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1180\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_engine\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mCParserWrapper\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1181\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1182\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mengine\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m\"python\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\user\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, src, **kwds)\u001b[0m\n\u001b[0;32m   2008\u001b[0m         \u001b[0mkwds\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"usecols\"\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0musecols\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2009\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2010\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_reader\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mparsers\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mTextReader\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msrc\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2011\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0munnamed_cols\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_reader\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0munnamed_cols\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2012\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader.__cinit__\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader._setup_parser_source\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'amazon.graph.large.csv'"
     ]
    }
   ],
   "source": [
    "drawPowerLawGraph('amazon.graph.large.csv')\n",
    "drawPowerLawGraph('amazon.graph.small.csv')\n",
    "drawPowerLawGraph('youtube.graph.large.csv')\n",
    "drawPowerLawGraph('youtube.graph.small.csv')\n",
    "drawPowerLawGraph('dblp.graph.large.csv')\n",
    "drawPowerLawGraph('dblp.graph.small.csv')\n",
    "drawPowerLawGraph('gnm1.csv')\n",
    "drawPowerLawGraph('gnm2.csv')\n",
    "drawPowerLawGraph('gnp1.csv')\n",
    "drawPowerLawGraph('gnp2.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c4344d17",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0b3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
