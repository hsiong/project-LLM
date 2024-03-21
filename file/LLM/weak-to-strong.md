> Reference: https://cdn.openai.com/papers/weak-to-strong-generalization.pdf

![Screenshot 2023-12-18 at 14 13 11](https://github.com/hsiong/project-LLM/assets/37357447/8cd09e2d-ba1e-45f2-b025-3296d681e7e4)

# INTRODUCTION

+ Problem with `superhuman models`

  However, superhuman models will be capable of complex and creative behaviors that humans can-
  not fully understand. For example, if a superhuman assistant model generates a million lines of ex-
  tremely complicated code, humans will not be able to provide reliable supervision for key alignment-
  relevant tasks, including: whether the code follows the user’s intentions, whether the assistant model
  answers questions about the code honestly, whether the code is safe or dangerous to execute, and
  so on. As a result, if we finetune a superhuman model with human supervision on a reward mod-
  eling (RM) or safety classification task, it is unclear how that model will generalize to complicated
  behaviors that humans could not reliably supervise themselves.

+ illustration

​	<u>using weak models to supervise strong models</u>.

+ Why should weak-to-strong learning be possible? 

  On the one hand, the strong model could simply
  learn to imitate the weak supervisor, including its errors, since that is what we would naively train
  it to do. On the other hand, strong pretrained models should already have good representations of
  the alignment-relevant tasks we care about. For example, if a model can generate complicated code,
  then it should intuitively also know whether that code faithfully adheres to the user’s instructions.
  <u>As a result, for the purposes of alignment we do not need the weak supervisor to teach the strong
  model new capabilities; instead, we simply need the weak supervisor to elicit what the strong model
  already knows.</u> This gives us hope that the strong model can generalize beyond the weak supervision,
  solving even hard problems for which the weak supervisor can only give incomplete or flawed
  training labels. We call this phenomenon weak-to-strong generalization

