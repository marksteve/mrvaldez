import random
import webbrowser


HOST = 'marksteve.github.com'


def cartwheel():
  # Some standards libraries are awesome
  # Think of them as pokemons
  # Gotta learn 'em all!
  webbrowser.open_new_tab('http://%s/mrvaldez/images/cartwheel.gif' % HOST)


def quote():
  quotes = """
  You can't win the internets
  You will all learn to MATH!
  """
  # You kind of have to work backwards to
  # figure out some functional programming code
  # Note the numbers prepending the comments
  return random.choice(
    filter(
      lambda line: line, # 3) The cleaned up list is then filtered for truthy values (non empty strings is what we're looking for) with a simple lambda that just returns the value
      map(
        lambda line: line.strip(), # 2) We clean up the list of lines by mapping it to a lambda that strips extra whitespacing
        quotes.split('\n') # 1) We start with a docstring split into lines
      )
    )
  )
