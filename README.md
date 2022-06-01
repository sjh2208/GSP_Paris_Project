# Do Frontoparietal Attentional Networks Underlie Phenomenal Consciousness? A Transcranial Magnetic Stimulation Study over the Intraparietal Sulcus

Imagine watching the sun set over the Hudson River on a clear summer night. The experience is visually stunning, bordering on overwhelming: the buildings along the opposing shore, the sparkling waves, the gradient from white to crimson to violet. How could one describe the enormity of such a scene? This rich visual consciousness seems to elude a comprehensive description of sufficient detail to convey the subjective experience. Now consider if this scene was frightful or anxiety-inducing rather than serene and the difficulty of conveying such an experience. Understanding how such subjective conscious experiences are generated in the brain is imperative for not only a basic-scientific understanding, but also for translational applications in treating disorders such as anxiety and depression which so drastically alter subjective experience (see Michel et al., 2019).

Researchers describe this discrepancy between our subjective perceptual experience and what is reportable from that experience as a discrepancy between phenomenal consciousness and access consciousness, respectively. However, what brain architectures support either of these flavors of conscious experience remains a topic of active debate. Some, such as Block (2011, 2014) and Lamme (2006), suggest that subjective, phenomenal consciousness is supported exclusively by early visual areas, and a bottleneck of information between these areas and higher, frontoparietal processing is what leads to the discrepancy with reportable, access consciousness. Others, such as Cohen & Dennett (2011) and Naccache (2018) suggest that no such dissociation between the two can be made. They defend this stance based on the apparent deficit in phenomenal consciousness in neglect disorders caused by lesions to parietal areas and the potential existence of low-resolution representations, still reportable by access consciousness, but not detailed enough to report with precision.

This project endeavors to find experimental evidence in favor of one of these views through a repetitive transcranial magnetic stimulation (rTMS) study over the intraparietal sulcus (IPS). Could rTMS over the IPS reduce the vividness of participants’ phenomenal consciousness? One possible mechanism by which phenomenal consciousness may arise is the spatial distribution of attention over visual scenes. Fiebelkorn et al. (2018) identify the IPS as playing a key role in the dynamics of attenuating and enhancing visual processing at attended locations, thereby incentivizng the shifting of attention around the visual field. Such fleeting directions of attention to locations outside of the focally-attended region may result in the numerous low-resolution representations Cohen & Dennett (2011) suggest contribute to the vividness of phenomenal consciousness. This previous work, as well as the deficits in visual consciousness associated with parietal lesions, lead me to hypothesize that inhibitory stimulation, like rTMS, over the IPS will reduce participants' ability to spatially distribute their attention over a complex visual scene and thereby reduce the vividness of their phenomenal consciousness. I predict that when asked to identify the predominant type of figure in a composite Sperling grid composed of numbers, letters, and shapes, participats' accuracy in making the correct identification will be significanly reduced following rTMS to the IPS (see Fig. 1, 2). This would suggest that the stimulation inhibited their ability to distribute their attention over the grid and indicate a reduction in the vividness of their visual phenomenal consciousness. Such a finding would support the view that phenomenal consciousness does indeed rely on architectures higher than early visual areas, and would thereby be evidence in favor of its non-dissociability from access consciousness.

**Fig. 1:**

![Fig. 1: rTMS design](https://github.com/sjh2208/GSP_Paris_Project/blob/main/rtms_design.png?raw=true)

**Fig. 2:**

![Fig. 2: trial design](https://github.com/sjh2208/GSP_Paris_Project/blob/main/trial_design.png?raw=true)


**References**

Block, N. (2011). Perceptual consciousness overflows cognitive access. _Trends in Cognitive Sciences_, 15(12), 567-575.

Block, N. (2014). Rich conscious perception outside focal attention. _Trends in Cognitive Sciences_, 18(9), 445-447.

Cohen, M., & Dennett, D. (2011). Consciousness cannot be separated from function. _Trends in Cognitive Sciences_, 15(8), 358-364.

Fiebelkorn, I. C., Pinsk, M. A., & Kastner, S. (2018). A dynamic interplay within the frontoparietal network underlies rhythmic spatial attention. _Neuron_, 99(4), 842-853.

Lamme, V. (2006). Towards a true neural stance on consciousness. _Trends in Cognitive Sciences_, 10(11), 494-501.

Naccache, L. (2018). Why and how access consciousness can account for phenomenal consciousness. _Phil. Trans. R. Soc. B_, 373(1755).

Michel, M., Beck, D., Block, N., Blumenfeld, H., Brown, R., Carmel, D., ... & Dehaene, S. (2019). Opportunities and challenges for a maturing science of consciousness. _Nature Human Behaviour_, 3(2), 104.

# Code Instructions

**Important: this experiment was designed and tested with PsychoPy3 v2021.2.3; it may not work with other versions!**

**Note: the data folder and clean_data.csv file have some pilot data included, simply delete these two and follow the instructions below to generate your own data.**

1. Generate the stimuli by running the **gen_stim.py** executable or the **Gen_Stim.ipynb** Jupyter notebook.
2. Open **exp_code.py** executable in PsychoPy and run through the PsychoPy Runner. The **test_exp.psyexp** builder file can be opened in the PsychoPy Builder to visualize the structure of the task, but should not be run.
3. Run either the **data_analysis.py** executable or the **Data_Analysis.ipynb** Jupyter notebook to update **clean_data.csv** with new data and visualize the results.
