

from subprocess import Popen, PIPE
import os
import uuid
import logging

log = logging.getLogger('torchbase.mapping')

def map(mapping_parameters):
    pass


def run_srst2(tor, locus_name, fastq1, fastq2=None):
    """
    Method to run srst2 using subprocess

    :return:
    """
    with tor.expose_torch_as_fasta(locus_name) as locus_file_path:
    #locus_file_path = tor.expose_torch_as_fasta(locus_name)
    # adds uuid to outfile name to make distinct
        outfile = os.path.join(os.path.dirname(locus_file_path), str(uuid.uuid1()))

        if not fastq2:
            command = ["srst2", "--input_se", fastq1, "--output", outfile, "--log", "--gene_db", locus_file_path]
        else:
            command = ["srst2", "--input_pe", fastq1, fastq2, "--output", outfile, "--log", "--gene_db", locus_file_path]

        process = Popen(command, stdout=PIPE, stderr=PIPE)
        (stdout, stderr) = process.communicate()
    log.info(stdout)
    if stderr:
        log.warn(stderr)
    return outfile + "__genes__resistance__results.txt"
