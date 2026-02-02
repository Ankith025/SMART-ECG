{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0e9ca10d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, request, flash, redirect\n",
    "import pickle\n",
    "import numpy as np\n",
    "from PIL import Image\n",
    "from tensorflow.keras.models import load_model\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5eb091ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b1aef1fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "def predict(values, dic):\n",
    "    if len(values) == 8:\n",
    "        model = pickle.load(open('models/diabetes.pkl','rb'))\n",
    "        values = np.asarray(values)\n",
    "        return model.predict(values.reshape(1, -1))[0]\n",
    "    elif len(values) == 26:\n",
    "        model = pickle.load(open('models/breast_cancer.pkl','rb'))\n",
    "        values = np.asarray(values)\n",
    "        return model.predict(values.reshape(1, -1))[0]\n",
    "    elif len(values) == 13:\n",
    "        model = pickle.load(open('models/heart.pkl','rb'))\n",
    "        values = np.asarray(values)\n",
    "        return model.predict(values.reshape(1, -1))[0]\n",
    "    elif len(values) == 18:\n",
    "        model = pickle.load(open('models/kidney.pkl','rb'))\n",
    "        values = np.asarray(values)\n",
    "        return model.predict(values.reshape(1, -1))[0]\n",
    "    elif len(values) == 10:\n",
    "        model = pickle.load(open('models/liver.pkl','rb'))\n",
    "        values = np.asarray(values)\n",
    "        return model.predict(values.reshape(1, -1))[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4b488974",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\")\n",
    "def home():\n",
    "    return render_template('home.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4d00ae35",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/diabetes\", methods=['GET', 'POST'])\n",
    "def diabetesPage():\n",
    "    return render_template('diabetes.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "32513585",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/cancer\", methods=['GET', 'POST'])\n",
    "def cancerPage():\n",
    "    return render_template('breast_cancer.html')\n",
    "\n",
    "@app.route(\"/heart\", methods=['GET', 'POST'])\n",
    "def heartPage():\n",
    "    return render_template('heart.html')\n",
    "\n",
    "@app.route(\"/kidney\", methods=['GET', 'POST'])\n",
    "def kidneyPage():\n",
    "    return render_template('kidney.html')\n",
    "\n",
    "@app.route(\"/liver\", methods=['GET', 'POST'])\n",
    "def liverPage():\n",
    "    return render_template('liver.html')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fa6d1873",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/malaria\", methods=['GET', 'POST'])\n",
    "def malariaPage():\n",
    "    return render_template('malaria.html')\n",
    "\n",
    "@app.route(\"/pneumonia\", methods=['GET', 'POST'])\n",
    "def pneumoniaPage():\n",
    "    return render_template('pneumonia.html')\n",
    "\n",
    "@app.route(\"/predict\", methods = ['POST', 'GET'])\n",
    "def predictPage():\n",
    "    try:\n",
    "        if request.method == 'POST':\n",
    "            to_predict_dict = request.form.to_dict()\n",
    "            to_predict_list = list(map(float, list(to_predict_dict.values())))\n",
    "            pred = predict(to_predict_list, to_predict_dict)\n",
    "    except:\n",
    "        message = \"Please enter valid Data\"\n",
    "        return render_template(\"home.html\", message = message)\n",
    "\n",
    "    return render_template('predict.html', pred = pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c2beb367",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/malariapredict\", methods = ['POST', 'GET'])\n",
    "def malariapredictPage():\n",
    "    if request.method == 'POST':\n",
    "        try:\n",
    "            if 'image' in request.files:\n",
    "                img = Image.open(request.files['image'])\n",
    "                img = img.resize((36,36))\n",
    "                img = np.asarray(img)\n",
    "                img = img.reshape((1,36,36,3))\n",
    "                img = img.astype(np.float64)\n",
    "                model = load_model(\"models/malaria.h5\")\n",
    "                pred = np.argmax(model.predict(img)[0])\n",
    "        except:\n",
    "            message = \"Please upload an Image\"\n",
    "            return render_template('malaria.html', message = message)\n",
    "    return render_template('malaria_predict.html', pred = pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ea894704",
   "metadata": {},
   "outputs": [
    {
     "ename": "AssertionError",
     "evalue": "View function mapping is overwriting an existing endpoint function: pneumoniapredictPage",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAssertionError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_13948/1296347090.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;33m@\u001b[0m\u001b[0mapp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mroute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"/pneumoniapredict\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmethods\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;34m'POST'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'GET'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mdef\u001b[0m \u001b[0mpneumoniapredictPage\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mrequest\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmethod\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m'POST'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[1;34m'image'\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrequest\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfiles\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mD:\\data\\lib\\site-packages\\flask\\app.py\u001b[0m in \u001b[0;36mdecorator\u001b[1;34m(f)\u001b[0m\n\u001b[0;32m   1313\u001b[0m         \u001b[1;32mdef\u001b[0m \u001b[0mdecorator\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mf\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1314\u001b[0m             \u001b[0mendpoint\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0moptions\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"endpoint\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1315\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0madd_url_rule\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mrule\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mendpoint\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1316\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1317\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mD:\\data\\lib\\site-packages\\flask\\app.py\u001b[0m in \u001b[0;36mwrapper_func\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m     96\u001b[0m                 \u001b[1;34m\"before the application starts serving requests.\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     97\u001b[0m             )\n\u001b[1;32m---> 98\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     99\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    100\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mupdate_wrapper\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mwrapper_func\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mD:\\data\\lib\\site-packages\\flask\\app.py\u001b[0m in \u001b[0;36madd_url_rule\u001b[1;34m(self, rule, endpoint, view_func, provide_automatic_options, **options)\u001b[0m\n\u001b[0;32m   1280\u001b[0m             \u001b[0mold_func\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mview_functions\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mendpoint\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1281\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mold_func\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mold_func\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[0mview_func\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1282\u001b[1;33m                 raise AssertionError(\n\u001b[0m\u001b[0;32m   1283\u001b[0m                     \u001b[1;34m\"View function mapping is overwriting an \"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1284\u001b[0m                     \u001b[1;34m\"existing endpoint function: %s\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0mendpoint\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAssertionError\u001b[0m: View function mapping is overwriting an existing endpoint function: pneumoniapredictPage"
     ]
    }
   ],
   "source": [
    "@app.route(\"/pneumoniapredict\", methods = ['POST', 'GET'])\n",
    "def pneumoniapredictPage():\n",
    "    if request.method == 'POST':\n",
    "        try:\n",
    "            if 'image' in request.files:\n",
    "                img = Image.open(request.files['image']).convert('L')\n",
    "                img = img.resize((36,36))\n",
    "                img = np.asarray(img)\n",
    "                img = img.reshape((1,36,36,1))\n",
    "                img = img / 255.0\n",
    "                model = load_model(\"models/pneumonia.h5\")\n",
    "                pred = np.argmax(model.predict(img)[0])\n",
    "        except:\n",
    "            message = \"Please upload an Image\"\n",
    "            return render_template('pneumonia.html', message = message)\n",
    "    return render_template('pneumonia_predict.html', pred = pred)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "\tapp.run(debug = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22c2f6a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "%tb\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
