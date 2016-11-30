print("Let's practice everything")
print('You\'d need to know \'bout escapes with \\ that do \nnewlines and \t tabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\t\twhere there is none.
"""
print("----------------\n"+poem+"\n-------------------")

number = 10 - 2 + 3 - 6
print("This should be five: %s" % number)

def secret_formula(started):
  jelly_beans = 500*started
  jars = jelly_beans / 1000
  crates = jars / 100
  return jelly_beans, jars, crates

start_point = 1000
jelly_beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" %start_point)
print("We'd have %d beans, %d jars, %d crates." %(jelly_beans, jars, crates))

start_point = start_point/10

print("We can also do it this way:")
print("We'd have %d beans, %d jars, %d crates" % secret_formula(start_point))
