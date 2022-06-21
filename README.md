# Do Frontoparietal Attentional Networks Underlie Phenomenal Consciousness? A Transcranial Magnetic Stimulation Study over the Intraparietal Sulcus

Imagine watching the sun set over the Hudson River on a clear summer night. The experience is visually stunning, bordering on overwhelming: the buildings along the opposing shore, the sparkling waves, the gradient from white to crimson to violet. How could one describe the enormity of such a scene? This rich visual consciousness seems to elude a comprehensive description of sufficient detail to convey the subjective experience. Now consider if this scene was frightful or anxiety-inducing rather than serene and the difficulty of conveying such an experience. Understanding how such subjective conscious experiences are generated in the brain is imperative for not only a basic-scientific understanding, but also for translational applications in treating disorders such as anxiety and depression which so drastically alter subjective experience (see Michel et al., 2019).

Researchers describe this discrepancy between our subjective perceptual experience and what is reportable from that experience as a discrepancy between phenomenal consciousness and access consciousness, respectively. However, what brain architectures support either of these flavors of conscious experience remains a topic of active debate. Some, such as Block (2011, 2014) and Lamme (2006), suggest that subjective, phenomenal consciousness is supported exclusively by early visual areas, and a bottleneck of information between these areas and higher, frontoparietal processing is what leads to the discrepancy with reportable, access consciousness. Others, such as Cohen & Dennett (2011) and Naccache (2018) suggest that no such dissociation between the two can be made, and that both varieties rely on global processing including frontoparietal networks. They defend this stance based on the apparent deficit in phenomenal consciousness in neglect disorders caused by lesions to parietal areas and the potential existence of low-resolution representations, still reportable by access consciousness, but not vivid enough to report with detailed precision.

This project endeavors to find experimental evidence in favor of one of these two mutually-exclusive theories regarding the distinction between access and phenomenal consciousness through a repetitive transcranial magnetic stimulation (rTMS) study over the intraparietal sulcus (IPS). To what extent will rTMS over the IPS reduce the vividness of participants’ phenomenal consciousness? One possible mechanism by which phenomenal consciousness may arise is the spatial distribution of attention over visual scenes. Fiebelkorn et al. (2018) identify the IPS as playing a key role in the dynamics of attenuating and enhancing visual processing at attended locations, thereby incentivizng the shifting of attention around the visual field. Such fleeting directions of attention to locations outside of the focally-attended region may result in the numerous low-resolution representations Cohen & Dennett (2011) suggest contribute to the vividness of phenomenal consciousness. 

This previous work, as well as the deficits in visual consciousness associated with parietal lesions, leads me to hypothesize that inhibitory stimulation, like rTMS, over the right IPS will reduce participants' ability to spatially distribute their attention over a complex visual scene and thereby reduce the vividness of their phenomenal consciousness. I predict that when asked to identify the predominant type of figure in a composite Sperling grid composed of numbers and letters, participats' accuracy in making the correct identification will be significanly reduced following rTMS to the right IPS (see Fig. 1, 2). Additionally, I predict that participants' subjective reports of the vividness of the stimuli will significantly decrease following the stimulation. This would suggest that the stimulation inhibited their ability to distribute their attention over the grid and indicate a reduction in the vividness of their visual phenomenal consciousness. Such a finding would support the view that phenomenal consciousness does indeed rely on architectures higher than early visual areas, and would thereby be evidence in favor of its non-dissociability from access consciousness.

**Fig. 1:**

![Fig. 1: rTMS design](https://github.com/sjh2208/GSP_Paris_Project/blob/main/rtms_design.png?raw=true)

**Fig. 2:**

![Fig. 2: trial design](https://github.com/sjh2208/GSP_Paris_Project/blob/main/trial_design.png?raw=true)

In order to test this hypothesis, I propose a two-by-two mixed factorial study design (see Fig. 3) testing the hit rates and subjective vividness reports of participants in the aforementioned task pre- and post-rTMS to the right IPS. Previous studies of TMS over parietal regions (see Bourgeois et al., 2013; Cappelletti et al., 2006; and Kanai et al., 2008) find the most significant effects on visual perception following stimulation of the right IPS over the left, presumably due to the right hemisphere's dominance in orienting attention. Using G\*Power (Faul et al., 2007), and approximating the eta-squared effect sizes found in these previous studies to be around 0.44 on average, I have determined that this study will require 36 healthy, adult participants who all pass the Transcranial Magnetic Stimulation Adult Safety Screen questionnaire (Keel et al., 2001) to acheive a desired power of 0.8.

**Fig. 3:**

![Fig. 3: study design](https://github.com/sjh2208/GSP_Paris_Project/blob/main/study_design.png?raw=true)

A rough outline, combining the information from Figures 1, 2, and 3 above, of the experiment is as follows: each of the participants will perform 50 trials of the task, with each duration of exposure at a random multiple of 25 ms in the range of 25 to 500 ms, prior to rTMS stimulation to their right IPS. A hit rate will then be calculated as the proportion of these 50 trials in which the participant correctly identified whether numbers or letters occupied most of the boxes in the grid. Then, following an offline session of rTMS to the right IPS, each participant will perform another 50 trials, again shown for random multiples of 25 ms. Then a new, post-rTMS hit rate can be calculated in the same manner as pre-rTMS. In terms of subjective reports, each participant will be asked to rate the vividness of the grid they saw after each trial under both stimulation conditions. An average-vividness score can then be compared across groups and sessions. 

Given the mixed factorial design, I will conduct a two-by-two repeated measures mixed ANOVA for differences in hit rate and subjective vividness both within- and between- participants. I expect a main effect of both session (within-participants) and stimulation validity (between-participants). I will also conduct a post-hoc analysis to determine the directionality of these differences, which I expect to reveal a decrease in hit rate and subjective vividness post-rTMS in the actual stimulation condition.

The experiment will be administered on a MacBook Air running the experiment code in PsychoPy3 v2021.2.3 (Peirce et al., 2019), data cleaning and compiling will be done using the scipy.stats and matplotlib.pyplot modules in Python via a Jupyter Notebook, and data visualization and analysis will be conducted in JASP (JASP Team, 2022). The grid stimuli were randomly generated using the Pillows module in Python via a Jupyter Notebook, specifying each to have a two-thirds majority of either shapes or numbers.

_Preliminary Results_
_Innovation_
_Potential Pitfalls and Contingency Strategies_

Link to my slides presenation on this project: https://docs.google.com/presentation/d/1sHPlPKrCcrFEbfyhWDobI4HJ01Q2_hHFpZsKIzpR4EM/edit?usp=sharing


**References**

Block, N. (2011). Perceptual consciousness overflows cognitive access. _Trends in Cognitive Sciences_, 15(12), 567-575.

Block, N. (2014). Rich conscious perception outside focal attention. _Trends in Cognitive Sciences_, 18(9), 445-447.

Bourgeois, A., Chica, A. B., Valero-Cabré, A., & Bartolomeo, P. (2013). Cortical control of inhibition of return: Causal evidence for task-dependent modulations by dorsal and ventral parietal regions. _Cortex_, 49, 2229-2238.

Cappelletti, M., Barth, H., Fregni, F., Spelke, E., & Pascual-Leone, A. (2006). rTMS over the intraparietal sulcus disrupts numerosity processing. _Experimental Brain Research_, 179, 631-642.

Cohen, M., & Dennett, D. (2011). Consciousness cannot be separated from function. _Trends in Cognitive Sciences_, 15(8), 358-364.

Fiebelkorn, I. C., Pinsk, M. A., & Kastner, S. (2018). A dynamic interplay within the frontoparietal network underlies rhythmic spatial attention. _Neuron_, 99(4), 842-853.

Faul, F., Erdfelder, E., Lang, A.-G., & Buchner, A. (2007). G\*Power 3: A flexible statistical power analysis program for the social, behavioral, and biomedical sciences. _Behavior Research Methods_, 39, 175-191.

JASP Team (2022). JASP (Version 0.16.3) \[Computer software\].

Kanai, R., Muggleton, N. G., & Walsh, V. (2008). TMS Over the Intraparietal Sulcus Induces Perceptual Fading. _Journal of Neurophysiology_, 100, 3343-3350.

Keel, J. C., Smith, M. J., & Wasserman, E. M. (2001). A safety screening questionnaire for transcranial magnetic stimulation. _Clinical Neurophysiology_, 112, 720.

Lamme, V. (2006). Towards a true neural stance on consciousness. _Trends in Cognitive Sciences_, 10(11), 494-501.

Michel, M., Beck, D., Block, N., Blumenfeld, H., Brown, R., Carmel, D., ... & Dehaene, S. (2019). Opportunities and challenges for a maturing science of consciousness. _Nature Human Behaviour_, 3(2), 104.

Naccache, L. (2018). Why and how access consciousness can account for phenomenal consciousness. _Phil. Trans. R. Soc. B_, 373(1755).

Peirce, J. W., Gray, J. R., Simpson, S., MacAskill, M. R., Höchenberger, R., Sogo, H., Kastman, E., & Lindeløv, J. (2019). PsychoPy2: experiments in behavior made easy. _Behavior Research Methods_.


# Code Instructions

**Important: this experiment was designed and tested with PsychoPy3 v2021.2.3; it may not work with other versions!**

**Note: the data folder and clean_data.csv file have some pilot data included, simply delete these two and follow the instructions below to generate your own data.**

1. Download all the files into one folder
2. Generate the stimuli by running the **gen_stim.py** executable or the **Gen_Stim.ipynb** Jupyter notebook.
3. Open **exp_code.py** executable in PsychoPy and run through the PsychoPy Runner. The **test_exp.psyexp** builder file can be opened in the PsychoPy Builder to visualize the structure of the task, but should not be run.
4. Run either the **data_prep.py** executable or the **Data_Prep.ipynb** Jupyter notebook to update with new data.
