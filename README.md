# Snowflake

**A super lightweight library to generate instagram-like unique IDs**

Python Snowflake is a super-light library that generates unique, Instagram-like IDs. I like the look of these IDs, and I
often use them on my project. After I wrote the same code for another project, I decided to create a public library for
that. Don't get too excited about this library. There are only 3 lines that generate uuid4 cut to 6 characters but do we
really need to write tons of code to make such a simple functionality?

## Installation Guide

Installation is super-easy. Just run the following command to install Python Snowflake from the PyPi repository

```
$ pip install python-snowflake
```

## Usage

```
>>> from snowflake import snowflake
>>> snowflake()
'4a82a1'
```
