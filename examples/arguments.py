from sysdig_tracers import Tracer, Args, ReturnValue

@Tracer(enter_args={"n": Args(0)}, exit_args={"ret": ReturnValue})
def factorial(n):
  return 1 if n == 1 else n * factorial(n-1)

print factorial(10)
