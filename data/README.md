###Usage

Before running LDA you need to format the dataset:

		python save_courses_as_text.py

Once you have extracted phi.json and theta.json from LDA you can zip all the data (metadata and theta):

		python generate_metadata.py

metadata contains all relevant information for each course:

		{
			"courses": [
				{
					"source": "coursera", 
					"video": "4cb0a880fc6111e3950b43bf39aa1bfd", 
					"name": "Social Entrepreneurship", 
					"image": "https://d15cw65ipctsrr.cloudfront.net/fa/b623100b2a11e491808b11e17df7d4/S-ent-pic.jpg", 
					"instructors": [], 
					"topics": [
						{"topicRef": "125", "prob": "0.037817440927028656"}, 
						{"topicRef": "21", "prob": "0.037183936685323715"}, 
						{"topicRef": "141", "prob": "0.03412659093737602"}, 
						{"topicRef": "93", "prob": "0.022117557004094124"}, 
						{"topicRef": "11", "prob": "0.021291246637701988"}, 
						{"topicRef": "55", "prob": "0.017297416925430298"}, 
						{"topicRef": "13", "prob": "0.01038395892828703"}, 
						{"topicRef": "62", "prob": "0.010025891475379467"}, 
						{"topicRef": "132", "prob": "0.009502561762928963"}, 
						{"topicRef": "70", "prob": "0.008483446203172207"}], 
					"affiliates": [
						{"image": "https://coursera-university-assets.s3.amazonaws.com/a1/26dc9b1295b7f1b521b1fa92d3873c/cbs-coursera-logo-square__1280x1280px.png", 
						"name": "Copenhagen Business School", 
						"id": 175}], 
					"description": "In this course you will learn how to create societal impact through Social Entrepreneurship (S-ENT). S-ENT describes the discovery and sustainable exploitation of opportunities to create social change. We will introduce you to S-ENT examples and guide you through the process of identifying an opportunity to address social problems as well as outlining your idea in a business plan."
				}, {
					"source": "coursera", 
					"video": "b4a3720051ad11e4b9b5a3dfc6bb5731", 
					"name": "Preparing for the AP* Calculus AB and BC Exams (Part 1 - Differential Calculus)"
					...
				}]
		}
