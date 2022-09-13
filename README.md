# RNA motif forces/word frequencies

Dimer "forces" are defined in the following paper:
Greenbaum BD, Cocco S, Levine AJ, Monasson R. Quantitative theory of entropic forces acting on constrained nucleotide sequences applied to viruses. Proc Natl Acad Sci USA. 2014 Apr 1;111(13):5054-9.

## Installation

### Docker
Build the image from `Dockerfile`:
```
docker build . -t DimerForces
```
The build is based on `debian:bullseye`

### Compilation: 
```
pip install . 
```
possibly with the `--user` option.

Old way calling `setup.py` directly:
```
python3 setup.py build && python3 setup.py install
```

## Usage:
* `CpG` force calculation in scanning window:
```
compute_sliding_window_force.py [-h] [-L WINDOW] [-c CONTIG] [-d DIMER] [-e END] [-s START] fasta_infile
```
Arguments `CONTIG` to use, `START`, `END` and `WINDOW` length are optional. `DIMER` defaults to `CG`.
Output: contig_id, start, #(valid dimers), dimer force.

* `CpG` force calculation for given coordinates:
```
compute_force_from_regions.py [-h] [-d DIMER] [-L MIN_LENGTH] [-s] fasta_infile coordinate_file
```
Input file format for `coordinate_file`:
```
contig	start	end	OTHER_OPTIONAL_COLUMNS
```
If `-s` is specified, strand (+/-) is needed as well:
```
contig	start	end	strand	OTHER_OPTIONAL_COLUMNS
```
Regions shorter than `MIN_LENGTH` are removed.
Output: the same as input plus an extra column with the force.
