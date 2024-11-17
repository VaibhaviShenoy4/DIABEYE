#Introduction
Diabetic Retinopathy (DR) is one of the leading causes of vision impairment and blindness among diabetic patients worldwide. 
Accurate and timely detection of DR can help in early intervention, significantly reducing the risk of severe outcomes. 
This project focuses on developing and evaluating a comprehensive deep learning framework, DIABEYE, to classify DR using retinal fundus images. We explore datasets from the coastal region of Mangalore, Karnataka, for real-time applicability and compare model performances across various datasets.

#Problem Statement
Diabetic Retinopathy detection often suffers from reduced accuracy due to the lack of regional specificity and diverse datasets.
There is a need for a reliable and accurate system that performs well on real-time data from specific geographic regions, such as the coastal area of Mangalore. Current methods lack comprehensive evaluation across diverse datasets.

#Objective
To design a robust diabetic retinopathy classification system that enhances accuracy for real-time datasets collected from the coastal region of Mangalore while performing a comparative analysis of four pre-trained deep learning models:
DenseNet121, MobileNet, VGG16, and InceptionV3.

#Methodology
1) Data Collection:
   - Real-time dataset from KS Hegde Hospital
   - Kaggle dataset with labeled severity levels
   - Merged dataset combining Kaggle and real-time data
2) Models Used for Comparative Study:
   - DenseNet121
   - MobileNet
   - VGG16
   - InceptionV3
3) Training and Evaluation:
The models were trained and tested on the three datasets: Real-time, Kaggle, and Merged.
Accuracy metrics were evaluated to identify the best-performing model.

#Results
DenseNet121 consistently outperformed the other models across all datasets, achieving the highest accuracy for the real-time data. This performance can be attributed to the similarity between the real-time and merged dataset's geographic region, highlighting the importance of dataset relevance.
#Future Scope
1. Dataset Expansion: Incorporate more real-time data from diverse geographic regions.
2. Model Optimization: Explore ensemble techniques and fine-tuning for further accuracy improvement.
3. Deployment: Develop an integrated web-based or mobile-friendly application for clinical use.
4. Explainability: Implement visualization techniques like Grad-CAM for better model interpretability in medical applications.



# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)

