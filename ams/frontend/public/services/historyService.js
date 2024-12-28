(function(window) {
    'use strict';

    function HistoryService() {
        this.STORAGE_KEY = 'ams_ai_history';
    }

    HistoryService.prototype.getHistory = function() {
        try {
            const history = localStorage.getItem(this.STORAGE_KEY);
            return history ? JSON.parse(history) : [];
        } catch (error) {
            console.error('Error:', error);
            return [];
        }
    };

    HistoryService.prototype.addToHistory = function(interaction) {
        try {
            const history = this.getHistory();
            const newInteraction = {
                ...interaction,
                timestamp: new Date().toISOString()
            };
            history.unshift(newInteraction);
            localStorage.setItem(this.STORAGE_KEY, JSON.stringify(history));
            return true;
        } catch (error) {
            console.error('Error:', error);
            return false;
        }
    };

    HistoryService.prototype.clearHistory = function() {
        try {
            localStorage.removeItem(this.STORAGE_KEY);
            return true;
        } catch (error) {
            console.error('Error:', error);
            return false;
        }
    };

    HistoryService.prototype.searchHistory = function(query) {
        try {
            const history = this.getHistory();
            return history.filter(item => 
                item.prompt.toLowerCase().includes(query.toLowerCase()) ||
                item.response.toLowerCase().includes(query.toLowerCase())
            );
        } catch (error) {
            console.error('Error:', error);
            return [];
        }
    };

    window.HistoryService = HistoryService;
})(window);
