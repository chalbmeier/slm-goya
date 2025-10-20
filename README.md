# Small Language Models for Producing Descriptions of Artwork

## Description

Out of interest, I experimented with SLMs for describing artwork. Automatically generated image descriptions can be useful for augmenting large image databases and improving their accessibility through semantic search. As a test case, I chose the work of Francisco de Goya's (1746–1828), whose paintings and drawings often feature grotesque figures that differ markedly from more common images found in typical training datasets. As an additional challenge, I decided to use a pre-trained model that could run on my laptop's 4 GB GPU. 

## Model Selection and Parameterization

After experimenting with different SLMs, I selected Hugging Face's [SmolVLM-500M-Instruct](https://huggingface.co/HuggingFaceTB/SmolVLM-500M-Instruct) model—a compact (~500 million parameters) multimodal model trained to generate image descriptions based on one or more input images and an instruction prompt. I found it better suited to my task than other models. For example, a [BLIP model trained for image captioning](https://huggingface.co/Salesforce/blip-image-captioning-large) produced reasonable but very short one-liners that omitted many details (e.g., "painting of a woman in a blue dress and feathered headdress"). In contrast, SmolVLM, when properly instructed, described the depicted figures, objects, and background in much greater detail. In fact, I had difficulties to rein it in and make it generate descriptions within the desired length of about 150 words.

The model's parameterization was largely dictated by the limitations of my hardware. My 4GB GPU could accomodate the model with default parameters and generate an image description in 7–10 seconds. However, I wanted to use beam search for text generation because it tends to produce [relatively generic and unsurprising](https://huggingface.co/blog/how-to-generate) texts—a desirable characteristic for text that feeds into a searchable image database. Beam search requires more GPU memory than the default greedy decoding, so I applied quantization and limited the number of beams to 4. As a result, inference time increased to roughly 60 seconds per 512x512 pixel image.

## Results

Prompted with the instruction "Describe the objects, people, and background you see in the painting or drawing in a factual manner.", the model was able to produce coherent and factual descriptions, particularly for paintings and drawings depicting human figures and a limited number of objects. For example, the model described the painting of [Queen of Spain Maria Louisa](https://www.wikidata.org/wiki/Q59260209) as follows:

 >The image depicts a portrait of a woman, likely from the 18th century, based on her attire and the style of the painting. The woman is positioned in the center of the frame, facing slightly to the right, with her head slightly tilted to the left. She has a serene expression on her face, with her eyes looking directly at the viewer. Her hair is styled in an elaborate manner, adorned with a large, wide-brimmed hat adorned with feathers and a blue ribbon. The hat appears to be made of fabric, possibly silk or a similar material, and has a high crown. The woman is wearing a corseted bodice with a corseted skirt that flows loosely around her body. The bodice is adorned with gold and silver embroidery, featuring intricate patterns and designs. She is also wearing a necklace with a pendant in the shape of a cross, which is a common symbol of Christianity. The background of the painting is dark

Cut-off text was a recurring issue, as the model was configured to produce a maximum of 200 tokens and tended to ignore instructions to keep descriptions short. Adjusting the prompt or a increasing the token limit could help mitigate this problem.  

The model also handled more unusual scenes with reasonable accuracy. For example the output for the drawing ["And So Was His Grandfather"](https://www.wikidata.org/wiki/Q64956388) was: 
> The image is a black-and-white drawing or painting of a donkey reading a book. The donkey is depicted in a seated position, wearing a long-sleeved shirt and pants. The donkey's ears are perked up, and it appears to be engaged in reading the book, which is held in its mouth. The donkey's expression is calm and focused, as if it is absorbed in the content of the book. In the background, there is a plain, neutral-toned wall, which provides a stark contrast to the donkey and the book. There are no other objects or figures in the image, keeping the focus solely on the donkey and the book. The drawing is done in a realistic style, with fine lines and shading to create depth and dimension. The donkey's fur is detailed, and the texture of its skin is discernible, giving it a lifelike appearance. The donkey's posture and the way it holds the book suggest that it might be

Accuracy declined in cases where objects were small, superimposed, or entangled. The model also struggled to correctly identify animal species, sometimes mistaking bats for birds, donkeys for horses, and apes for humans. In one case, it "recognized" a kangaroo in Goya's work (["Neither More nor Less"](https://www.wikidata.org/wiki/Q64956396)):

>The image is a black-and-white drawing or painting. In the foreground, there is a kangaroo sitting on its haunches. The kangaroo appears to be looking down at a human who is kneeling on the ground in front of it. The human is wearing a hat and appears to be interacting with the kangaroo. In the background, there is a structure that looks like a barrel or a barrel-like object. There is text at the bottom of the image that reads "Ni mea ni menos," which translates to "No, no, no" in English. ### Analysis and Description: 1. **Subjects and Objects**: - **Kangaroo**: The kangaroo is the main subject of the image. It is depicted in a squatting position, facing the human who is kneeling. - **Human**: The human is kneeling on the ground in front of the kangaroo. He is wearing a hat and appears to be interacting with the kangaroo.

This example also illustrates that model had rudimentary capabilities in text formatting, optical character recognition (OCR), and translation.

## Conclusion
Overall, it is remarkable what a SLM and just 4GB of GPU memory can achieve. However, the output quality is still insufficient for reliable use. Subsatnial improvement would likely require either a larger model or one specicifically trained for this task—generating medium-length descriptions of artworks. 

## Sources & Credits

**Artwork metadata:**  
Retrieved from [Wikidata](https://www.wikidata.org) (accessed October 2025).  
Wikidata content is available under the [Creative Commons CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) license.

**Images:**  
Downloaded from [Wikimedia Commons](https://commons.wikimedia.org) and linked through their corresponding [Wikidata](https://www.wikidata.org) entries.  
Each image retains its original license as specified on Wikimedia Commons.  

**Note:**  
All generated image descriptions were produced using the [SmolVLM-500M-Instruct](https://huggingface.co/HuggingFaceTB/SmolVLM-500M-Instruct) model for research and educational purposes.

