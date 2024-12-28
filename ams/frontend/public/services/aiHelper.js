// AIHelper service
(function(window) {
    'use strict';

    function AIHelper() {
        this.API_KEY = 'AIzaSyCEalrKbuNPw_8LkkpRELKccwdx7yAewfY';
        this.API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent';
    }

    AIHelper.prototype.generateResponse = async function(prompt) {
        try {
            const response = await fetch(`${this.API_URL}?key=${this.API_KEY}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    contents: [{
                        parts: [{
                            text: prompt
                        }]
                    }]
                })
            });

            const data = await response.json();
            return data.candidates[0].content.parts[0].text;
        } catch (error) {
            console.error('Error:', error);
            return 'Sorry, an error occurred while processing your request.';
        }
    };

    AIHelper.prototype.analyzeAffiliate = async function(affiliateData) {
        const prompt = `Analyze this affiliate data: ${JSON.stringify(affiliateData)}`;
        return this.generateResponse(prompt);
    };

    AIHelper.prototype.suggestImprovements = async function(affiliateData) {
        const prompt = `Suggest improvements for this affiliate program: ${JSON.stringify(affiliateData)}`;
        return this.generateResponse(prompt);
    };

    AIHelper.prototype.generateContent = async function(topic) {
        const prompt = `Generate marketing content about: ${topic}`;
        return this.generateResponse(prompt);
    };

    window.AIHelper = AIHelper;
})(window);
