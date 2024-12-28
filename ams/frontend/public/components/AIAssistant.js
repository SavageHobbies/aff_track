import React, { useState, useEffect } from 'react';

// AIAssistant component
const AIAssistant = () => {
    const [aiHelper] = React.useState(new window.AIHelper());
    const [historyService] = React.useState(new window.HistoryService());
    const [prompt, setPrompt] = React.useState('');
    const [response, setResponse] = React.useState('');
    const [isLoading, setIsLoading] = React.useState(false);
    const [showHistory, setShowHistory] = React.useState(false);
    const [history, setHistory] = React.useState([]);

    React.useEffect(() => {
        setHistory(historyService.getHistory());
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!prompt.trim()) return;

        setIsLoading(true);
        try {
            const result = await aiHelper.generateResponse(prompt);
            setResponse(result);
            historyService.addToHistory({ prompt, response: result });
            setHistory(historyService.getHistory());
        } catch (error) {
            console.error('Error:', error);
            setResponse('Sorry, an error occurred while processing your request.');
        }
        setIsLoading(false);
    };

    return (
        <div className="p-6">
            <div className="max-w-4xl mx-auto">
                <h1 className="text-2xl font-bold mb-6">AI Assistant</h1>
                
                <div className="mb-6">
                    <form onSubmit={handleSubmit} className="space-y-4">
                        <textarea
                            value={prompt}
                            onChange={(e) => setPrompt(e.target.value)}
                            className="w-full p-3 border rounded-lg"
                            rows="4"
                            placeholder="Enter your prompt here..."
                        />
                        <div className="flex justify-between">
                            <button
                                type="submit"
                                disabled={isLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
                            >
                                {isLoading ? 'Processing...' : 'Submit'}
                            </button>
                            <button
                                type="button"
                                onClick={() => setShowHistory(!showHistory)}
                                className="px-4 py-2 bg-gray-600 text-white rounded hover:bg-gray-700"
                            >
                                {showHistory ? 'Hide History' : 'Show History'}
                            </button>
                        </div>
                    </form>
                </div>

                {response && (
                    <div className="bg-white p-4 rounded-lg shadow mb-6">
                        <h2 className="font-bold mb-2">Response:</h2>
                        <div className="whitespace-pre-wrap">{response}</div>
                    </div>
                )}

                {showHistory && (
                    <div className="bg-white p-4 rounded-lg shadow">
                        <h2 className="font-bold mb-4">History</h2>
                        <div className="space-y-4">
                            {history.map((item, index) => (
                                <div key={index} className="border-b pb-4">
                                    <p className="font-medium">Prompt: {item.prompt}</p>
                                    <p className="mt-2">Response: {item.response}</p>
                                    <p className="text-sm text-gray-500 mt-1">
                                        {new Date(item.timestamp).toLocaleString()}
                                    </p>
                                </div>
                            ))}
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

// Make AIAssistant available globally
window.AIAssistant = AIAssistant;
