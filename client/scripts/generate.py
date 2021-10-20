"""
CLI Tool for working with this project
"""
from fire import Fire
import string
import re
from os import path, makedirs
from rich.console import Console

from .assets import generator_strings as codes

class Generator:
  """
  Generate files needed for development
  """

  def method(self, module: str, name: str, model: str = None, endpoint: str = None):
    """Generate method for a module"""
    console = Console()
    # set model as name if its none
    model = name if model is None else model
    # get method name
    name = re.sub(r"[^a-z]+", ' ', name).strip()
    method_name = name.replace(' ', '_')
    description = name.capitalize()
    endpoint_key = method_name.upper()
    # get model name
    model = re.sub(r"[^a-z]+", ' ', model).strip()
    model_name = string.capwords(model).replace(' ', '')
    # get datasource path
    module = re.sub(r"[^a-z]+", ' ', module).strip()
    module_name = module.replace(' ', '_')
    datasource_path = path.join('py_client', 'modules', module_name, 'datasource.py')
    endpoints_path = path.join('py_client', 'modules', module_name, 'endpoints.py')
    content = codes.METHOD.format(name=method_name, description=description, model=model_name, endpoint=endpoint_key)
    # write code
    if path.exists(datasource_path) and (path.exists(endpoints_path) or endpoint is None):
      console.print(f"Adding method [b green]{method_name}[/b green] in module [b blue]{module_name}[/b blue]\n")
      # update datasource
      with open(datasource_path, 'a') as dsfile:
        console.print(f"[yellow][UPDATING][/yellow]\t[violet]{datasource_path}[/violet]")
        dsfile.write(content)
      # update endpoint
      if endpoint:
        with open(endpoints_path, 'a') as epfile:
          console.print(f"[yellow][UPDATING][/yellow]\t[violet]{endpoints_path}[/violet]")
          epfile.write(f"\n{endpoint_key} = '{endpoint}'")
    else:
      console.print(f'[ERROR] path does not exist {path.abspath(datasource_path)}', style='red')


  def model(self, module: str, name: str):
    """Generate a model file"""
    console = Console()

    name = re.sub(r"[^a-z]+", ' ', name).strip()
    classname = string.capwords(name).replace(' ', '')
    filename = name.replace(' ', '_')
    # get module path
    module = re.sub(r"[^a-z]+", ' ', module).strip()
    module_name = module.replace(' ', '_')
    models_path = path.join('py_client', 'modules', module_name, 'models')
    if path.exists(models_path):
      console.print(f"Generating model [b green]{filename}[/b green] in module [b blue]{module_name}[/b blue]\n")
      # create file
      model_path = path.join(models_path, filename + '.py')
      console.print(f"[green][CREATING][/green]\t[violet]{model_path}[/violet]")
      with open(model_path, 'w+') as pyfile:
        pyfile.write(codes.MODEL.format(classname=classname, name=name))
      # update model init
      model_init_path = path.join(models_path, '__init__.py')
      with open(model_init_path, 'a') as mfile:
        console.print(f"[yellow][UPDATING][/yellow]\t[violet]{model_init_path}[/violet]")
        mfile.writelines(f"\nfrom .{filename} import *")
    else:
      console.print(f'[ERROR] path does not exist {path.abspath(models_path)}', style='red')

  def module(self, name: str):
    """Generate a new module"""
    console = Console()
    
    name = re.sub(r"[^a-z]+", ' ', name).strip()
    classname = string.capwords(name).replace(' ', '')
    module_name = name.replace(' ', '_')
    # Find paths
    module_path = path.join('py_client', 'modules', module_name)
    # components of module
    comps = {
      "module": module_path,
      "datasource": path.join(module_path, 'datasource.py'),
      "endpoints": path.join(module_path, 'endpoints.py'),
      "init": path.join(module_path, '__init__.py'),
      "models": path.join(module_path, 'models'),
      "models_init": path.join(module_path, 'models', '__init__.py')
    }
    # codemap
    codemap = {
      "datasource": codes.DATASOURCE,
      "endpoints": codes.ENDPOINTS,
      "init": codes.INIT,
      "models_init": codes.MODELS_INIT
    }
    if not path.exists(module_path):
      # create the folder
      console.print(f"Generating module [b green]{module_name}[/b green]\n")
      for key, value in comps.items():
        console.print(f"[green][CREATING][/green]\t[violet]{value}[/violet]")
        if key == 'module':
          makedirs(value)
        elif key == 'models':
          makedirs(value)
        elif key in codemap:
          with open(value, "w") as pyfile:
            pyfile.write(codemap[key].format(classname=classname, module=module_name))
      # update modules __init__.py
      modules_init_path = path.join('py_client', 'modules', '__init__.py')
      with open(modules_init_path, 'a') as mfile:
        console.print(f"[yellow][UPDATING][/yellow]\t[violet]{modules_init_path}[/violet]")
        mfile.writelines(f"\nfrom .{module_name} import *")
    else:
      console.print(f'[ERROR] folder already exists {path.abspath(module_path)}', style='red')

def main():
  Fire(Generator)