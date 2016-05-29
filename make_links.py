import os
import json
import shutil

link_file = "links.json"

def run():

  print("Gathering directories...")
  file_path = os.path.realpath(__file__)
  dir_path  = os.path.dirname(file_path)
  home_path = os.path.expanduser("~")

  print("Loading link data ({})...".format(link_file))
  with open(link_file) as f:
    data = json.loads(f.read())

  # path from users home directory to where this directory should be symlinked
  link_to_repo = data["link_to_repo"]
  full_link_to_repo = os.path.join(home_path, link_to_repo)
  # dictionary of paths in this directory related to where they should be symlinked
  # from the users home directory
  config_links = data["config_links"]

  text = []
  add_text = text.append

  add_text("Install links from this directory to this user directory?")
  add_text("\tthis dir:   {}".format(dir_path))
  add_text("\ttarget dir: {}".format(home_path))
  add_text("")
  add_text("Links to be created:")

  links = {}

  # if this repo is somewhere other then the link location, make the needed link
  if dir_path != full_link_to_repo:
    links[dir_path] = full_link_to_repo
    add_text("\t{}\t=>\t{}".format(full_link_to_repo, dir_path))

  for source, target in config_links.iteritems():
    full_source = os.path.join(dir_path, source)
    full_target = os.path.join(home_path, target)
    links[full_source] = full_target
    add_text("\t{}\t=>\t{}".format(full_target, full_source))
 
  add_text("\nContinue? [y/n]")

  for t in text:
    print(t)

  user_choice = raw_input()

  if user_choice != "y":
    print("exiting...")
    exit()


  for source, target  in links.iteritems():
    print("Linking: {}\t=>\t{}".format(target, source))

    if os.path.islink(target):
      os.unlink(target)
    if os.path.isdir(target):
      shutil.rmtree(target)
    if os.path.exists(target):
      os.remove(target)
    
    os.symlink(source, target)

  print("Done!")

if __name__ == "__main__":
  run()
