# BLiMP-NL (Dutch BLIMP)

### Paper

Title: `BLiMP-NL: The Benchmark of Linguistic Minimal Pairs for Dutch`

Abstract: https://osf.io/preprints/psyarxiv/mhjbx_v2

Homepage: https://data.ru.nl/collections/ru/cls/blimp-nl_dsc_550

Dataset: https://huggingface.co/datasets/juletxara/blimp-nl

BLiMP-NL is a dataset of Dutch linguistic minimal pairs for evaluating language models' syntactic knowledge. The dataset contains minimal pairs for 22 grammatical phenomena in Dutch, further divided into 84 paradigms, with a total of 8,400 minimal pairs.

### Citation

```
@article{suijkerbuijk2023blimp,
  title={BLiMP-NL: The Benchmark of Linguistic Minimal Pairs for Dutch},
  author={Suijkerbuijk, M.J.P.F. and Prins, Zoë and de Heer Kloots, Marianne and Zuidema, Willem and Frank, Stefan},
  year={2023}
}
```

### Groups and Tasks

#### Groups

* `blimp_nl`

#### Tasks

* `blimp_nl_anaphor_agreement`: Tests anaphor agreement phenomena
* `blimp_nl_binding_principle_a`: Tests binding principle A constraints
* `blimp_nl_argument_structure`: Tests argument structure and transitivity
* `blimp_nl_complementive`: Tests complementive constructions
* `blimp_nl_passive`: Tests passive voice constructions
* `blimp_nl_infinitival_argument_clause`: Tests infinitival argument clauses
* `blimp_nl_finite_argument_clause`: Tests finite argument clauses
* `blimp_nl_auxiliaries`: Tests auxiliary verb constructions
* `blimp_nl_adverbial_modification`: Tests adverbial modification structures
* `blimp_nl_verb_second`: Tests verb-second order constraints
* `blimp_nl_wh_movement`: Tests wh-movement and question formation
* `blimp_nl_wh_movement_restrictions`: Tests restrictions on wh-movement
* `blimp_nl_relativization`: Tests relative clause formation
* `blimp_nl_topicalization`: Tests topicalization structures
* `blimp_nl_parasitic_gaps`: Tests parasitic gap constructions
* `blimp_nl_r_words`: Tests r-word (er-word) phenomena
* `blimp_nl_nominalization`: Tests nominalization processes
* `blimp_nl_determiners`: Tests determiner usage and constraints
* `blimp_nl_quantifiers`: Tests quantifier scope and interpretation
* `blimp_nl_adpositional_phrases`: Tests adpositional phrase structures
* `blimp_nl_crossing_dependencies`: Tests crossing dependency constraints
* `blimp_nl_extraposition`: Tests extraposition phenomena

The dataset includes 8,400 validated minimal pairs testing various Dutch linguistic phenomena:

- **Syntactic phenomena**: Argument structure, binding principles, complementive constructions
- **Movement phenomena**: Wh-movement, topicalization, relativization, extraposition
- **Agreement phenomena**: Anaphor agreement, verb-second constraints
- **Clause types**: Finite and infinitival argument clauses, passive constructions
- **Lexical phenomena**: Auxiliaries, determiners, quantifiers, r-words, nominalization
- **Complex structures**: Parasitic gaps, crossing dependencies, adverbial modification

### Checklist

For adding novel benchmarks/datasets to the library:
* [x] Is the task an existing benchmark in the literature?
  * [x] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?

If other tasks on this dataset are already supported:
* [x] Is the "Main" variant of this task clearly denoted?
* [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [x] Have you noted which, if any, published evaluation setups are matched by this variant?
