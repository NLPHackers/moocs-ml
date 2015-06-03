###Usage

* Get mallet:

		bash fetchMallet.sh

* Run LDA, be sure to visit the data folder and format the dataset. Then run:

		python training/mallet_processor.py <numTopics> <numIterations> <dataPath>

* Anotate trained_model/phi.xml adding a category and a name to each topic, for instance: 

		category="2" name="Astronomy"

* Transform phi.xml as phi.json:

		python trained_model/xml2json.py -t xml2json -o phi.json phi.xml

* Filter phi.json to get the topics_data.json file to push to the database:

		python trained_model/format_phi.py

* Read theta.txt and save it as json:

		python trained_model/format_theta.py

You can then use phi.json and theta.json to generate metadata.json and push it to the database.



topics_data.json contains relevant data for each topic:

		[
			{
				"topbigrams": 
					[{"bigram": "confidence interval", "prob": 0.0032414910858995136}, 
					{"bigram": "blood pressure", "prob": 0.00226904376012966}, 
					{"bigram": "sample size", "prob": 0.0021609940572663426}, 
					{"bigram": "relative risk", "prob": 0.0021609940572663426}, 
					{"bigram": "standard error", "prob": 0.0019448946515397082},
					{"bigram": "standard deviation", "prob": 0.001728795245813074}, 
					{"bigram": "standard errors", "prob": 0.001728795245813074}], 
				"category": "Science", 
				"_id": "0", 
				"topwords": [{"word": "sample", "prob": 0.03016754099610045}, 
					{"word": "group", "prob": 0.015242547029608648}, 
					{"word": "difference", "prob": 0.015191738539509952}, 
					{"word": "standard", "prob": 0.014251781472684086}, 
					{"word": "data", "prob": 0.014023143267239956}, 
					{"word": "population", "prob": 0.013362632895956914}, 
					{"word": "study", "prob": 0.012765633137297243}], 
				"name": "Statistics and biology"
			},{ 
				...
			}
		] 


