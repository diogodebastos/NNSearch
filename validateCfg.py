import commonFunctions as funk

if __name__ == "__main__":
  import argparse
  import os.path

  parser = argparse.ArgumentParser(description='Process the command line options')
  parser.add_argument('-c', '--configFile', required=True, help='Configuration file describing the neural network topology and options as well as the samples to process')
  parser.add_argument('-v', '--verbose', action='store_true', help='Whether to print verbose output')

  args = parser.parse_args()

  if not os.path.isfile(args.configFile):
    import errno
    #raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), args.configFile)
    raise OSError(errno.ENOENT, os.strerror(errno.ENOENT), args.configFile)


  validator = funk.NetworkBuilder(args.configFile, batch=True, verbose=args.verbose)

