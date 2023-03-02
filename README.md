# SuperLim 2

See a general description of the benchmark [here](https://spraakbanken.gu.se/resurser/superlim). The link to the paper will be added soon.

See the brief overview of the tasks and datasets [here](https://github.com/spraakbanken/SuperLim-2/blob/main/tasks.tsv). 

See the detailed instruction for dataset developers below, it makes the format requirements very clear.

**General file requirements:**

Encoding: UTF-8.

File format: JSONL is obligatory; TSV is welcome.

Train, dev and test must be separate files, which have the same structure.

File names must be "&lt;name>\_&lt;split>.&lt;ext>" (avoid underscores (\_) in the &lt;name>), where 
- &lt;split> is either "train", "dev" or "test", and 
- &lt;ext> is either "tsv" or "jsonl". 

If the dataset contains more than one tasks, add "_taskname" to the file name. File names should be lowercased.

Documentation sheets are obligatory, the name must be "&lt;name>_documentation-sheet.tsv". If you have to add more files to your data, name them in a transparent manner and list them in the documentation sheet.

**Requirements for the different file formats**

For both formats:
- Column names in TSV and attribute names in JSONL must be in lowercase and without spaces. They must adhere to the following regexp: `[a-z_][a-z0-9_]*`. This is to ensure that they can be easily read by (hopefully) any major programming language. The names must be in English and preferably be self-explanatory.

For JSONL:
- Each line is a valid JSON object, with the same structure. That is, the top level objects have the same keys defined with the same type of value. Explicitly use `null` to mark the absence of a value or a "zero-like value" of the right type (for instance `comment: ""` for an object that does not have a comment associated with it, or `links: []` for an object without any links). If a value is not `null`, the user must be able to use the object as if it is complete (and not have to guess if a zero-like value is just zero or whether it represents a missing value).
- Values of the top-level objects can be of any valid JSON type. Prefer to use array values for keys that are associated with a differing number of items between lines.

For TSV:
- Rows are on separate lines. Both CRLF and LF line endings are allowed, but not mixed in one file.
- Columns are separated by tab characters (HT).
- CRLF, LF and HT are never part of the data.
- Fields are not quoted (that is: don't use text delimiters). Any quotation marks in the TSV are therefore part of the data.
- The first line in the TSV file is a header, with a name for each column (see above).
- Comment lines are not allowed in the TSV file. Put such information in the documentation sheet or in a separate documentation file if needed. If you have additional documentation, its existence must be mentioned in the documentation sheet. If you find you frequently need to comment single rows, consider using a comment column. 
- TSVs can be in wide format or long format. Make sure that is it clear from the documentation how to interpret the table.
- TSVs should be rectangular – every row has an equal number of fields. Empty fields are allowed. 