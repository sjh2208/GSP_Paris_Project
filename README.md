# Do Frontoparietal Attentional Networks Underlie Phenomenal Consciousness? A Transcranial Magnetic Stimulation Study of the Intraparietal Sulcus

Consider watching the sun set over the Hudson River on a clear summer night. The experience is visually stunning, bordering on overwhelming: the buildings along the opposing shore, the sparkling waves, the gradient from white to crimson to violet. How could one describe the enormity of such a scene? This rich visual consciousness seems to elude a comprehensive description of sufficient detail to convey the subjective experience. Now, imagine that this scene was frightful or anxiety-inducing rather than serene. Understanding how subjective conscious experiences are generated in the brain is imperative for not only a basic-scientific understanding, but also for translational applications in treating disorders such as anxiety and depression which so drastically alter subjective experience.

Researchers describe this discrepancy between our subjective perceptual experience and what is reportable from that experience as a discrepancy between phenomenal consciousness and access consciousness, respectively. However, what brain architectures support either of these flavors of conscious experience—and whether or not they are dissociable functions—remains a topic of active debate. Some, such as Block (2011, 2014) and Lamme (2006), suggest that subjective, phenomenal consciousness is supported exclusively by early visual areas, and a bottleneck of information between these areas and higher, frontoparietal processing is what leads to the discrepancy with reportable, access consciousness. Others, such as Cohen & Dennett (2011) and Naccache (2018) suggest that no such dissociation between the two can be made. They defend this stance on the grounds of the impossibility to experimentally verify any discrepancy, as well as the apparent deficit in phenomenal consciousness in neglect disorders caused by lesions to parietal areas.

This project endeavors to support the latter view through a repetitive transcranial magnetic stimulation study over the intraparietal sulcus, a region implicated in neglect disorders such as hemispatial neglect and Balint's syndrome. I hypothesize that such inhibitory stimulation will reduce participants' ability to spatially distribute their attention over a complex visual scene, such as a composite Sperling grid with numbers, letters, and shapes. Such a finding would support the view that phenomenal consciousness does indeed rely on architectures higher than early visual areas, and would be evidence in favor of its non-dissociability from access consciousness.

**References**

Block, N. (2011). Perceptual consciousness overflows cognitive access. Trends in Cognitive Sciences, 15(12), 567-575.

Block, N. (2014). Rich conscious perception outside focal attention. Trends in Cognitive Sciences, 18(9), 445-447.

Cohen, M., & Dennett, D. (2011). Consciousness cannot be separated from function. Trends in Cognitive Sciences, 15(8), 358-364.

Lamme, V. (2006). Towards a true neural stance on consciousness. Trends in Cognitive Sciences, 10(11), 494-501.

Naccache, L. (2018). Why and how access consciousness can account for phenomenal consciousness. Phil. Trans. R. Soc. B, 373(1755).

# Code Instructions

**Important: this experiment was designed with PsychoPy3 v2021.2.3; it may not work with other versions!**

1. Generate the stimuli by running the **gen_stim.py** executable or the **Gen_Stim.ipynb** Jupyter notebook.
2. Open **exp_code.py** executable in PsychoPy and run through the PsychoPy Runner. The **test_exp.psyexp** builder file can be opened in the builder to visualize the structure of the task, but should not be run.
3. Run either the **data_analysis.py** executable or the **Data_Analysis.ipynb** Jupyter notebook to update **clean_data.csv** with new data and visualize the results.
