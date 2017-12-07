import commonFunctions as funk

if __name__ == "__main__":
  import argparse
  import os.path

  parser = argparse.ArgumentParser(description='Process the command line options')
  parser.add_argument('-d', '--dryRun', action='store_true', help='Do a dry run (i.e. do not actually run the potentially dangerous commands but print them to the screen)')
  parser.add_argument('-c', '--configFile', required=True, help='Configuration file describing the neural network topology and options as well as the samples to process')
  parser.add_argument('-v', '--verbose', action='store_true', help='Whether to print verbose output')
  parser.add_argument('-o', '--outDirectory', required=True, help='Name of the output directory')

  args = parser.parse_args()

  if not args.dryRun:
    print "You did not enable dry run. You are on your own!"

  if not os.path.isfile(args.configFile):
    import errno
    #raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), args.configFile)
    raise OSError(errno.ENOENT, os.strerror(errno.ENOENT), args.configFile)

  import json
  configJson = json.load(open(args.configFile, "rb"))
  if args.verbose:
    print json.dumps(configJson, indent=4)

  samples = {}
  for samp in configJson["network"]["samples"]:
    samples[samp["name"]] = samp
    samples[samp["name"]]["json"] = json.load(open(samp["file"], "rb"))

  if args.verbose:
    print json.dumps(samples, indent=3)

