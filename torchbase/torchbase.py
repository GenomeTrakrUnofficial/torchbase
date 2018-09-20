import docpie

version = "0.1a"

"""
Usage:
  torchbase [options]
  torchbase run [options] DATABASE FILE1 [FILE2...]
  torchbase pull [options] DATABASE
  torchbase convert [options] FASTA_FILE PROFILE_FILE DATABASE_NAME
  torchbase update [options] DATABASE_DIR DATABASE

Options:
  -h -? --help    Show this screen
  -v --version    Show software [and database] version

"""


"""command-decorator, allows subcommands to be obvious in-line, and
   binds argparse argument namespace to declared function parameters.
   ---JSP 2018-09-20
"""

def command(name):
	def command_decorator(func):
	@wraps(func)
	def wrapped_command(namespace, *args, **kwargs):
		#set logging level
		for log_level, i in zip((WARNING, INFO, DEBUG), range(0, namespace.verbose or 0)): #shorter than a bunch of if-else statements
			log.setLevel(log_level) #verbose = 0, log level is at logging.ERROR; verbose=3 or more, log level is at DEBUG
			log.warning("setting log level:" + str(log_level))
		#test if being piped to
		if not isatty(0):
			ids = [str(idd).strip() for idd in stdin]
			if hasattr(namespace, 'slims_barcodes'):
				namespace.slims_barcodes += ids
			else:
				namespace.slims_barcodes = ids
			if hasattr(namespace, 'names'):
				namespace.names += ids
		for k,v in kwargs.items():
			setattr(namespace, k, v)
		[print(f) for f in func(argv=args, **vars(namespace))]
	return wrapped_command
return command_decorator








def main():
	#do stuff


if __name__ == '__main__':
	
	
