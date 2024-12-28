function LinkManager() {
    const [links, setLinks] = useState([
        {
            id: 1,
            name: "Gaming Laptop Review",
            program: "Amazon Associates",
            originalUrl: "https://amazon.com/dp/B01234567",
            affiliateUrl: "https://amazon.com/dp/B01234567?tag=mysite-20",
            clicks: 145,
            earnings: 23.50,
            lastClick: "2024-12-26",
            category: "Tech",
            tags: ["laptop", "gaming"]
        },
        {
            id: 2,
            name: "Shopify Tutorial",
            program: "Shopify Partners",
            originalUrl: "https://shopify.com/pricing",
            affiliateUrl: "https://shopify.com/pricing?ref=mysite",
            clicks: 89,
            earnings: 150.00,
            lastClick: "2024-12-26",
            category: "Software",
            tags: ["ecommerce", "tutorial"]
        }
    ]);

    const [showCreateModal, setShowCreateModal] = useState(false);
    const [selectedCategory, setSelectedCategory] = useState('all');

    const categories = ["All", "Tech", "Software", "Fashion", "Home"];

    const handleCopyLink = (url) => {
        navigator.clipboard.writeText(url);
        // Show success toast
    };

    const handleCreateLink = (newLink) => {
        setLinks(prevLinks => [...prevLinks, { ...newLink, id: prevLinks.length + 1 }]);
        setShowCreateModal(false);
    };

    return (
        <div className="p-6">
            <div className="mb-6 flex justify-between items-center">
                <h1 className="text-2xl font-semibold">Link Manager</h1>
                <div className="flex gap-4">
                    <select 
                        className="px-3 py-2 border rounded-lg"
                        value={selectedCategory}
                        onChange={(e) => setSelectedCategory(e.target.value)}
                    >
                        {categories.map(cat => (
                            <option key={cat} value={cat.toLowerCase()}>
                                {cat}
                            </option>
                        ))}
                    </select>
                    <button 
                        className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
                        onClick={() => setShowCreateModal(true)}
                    >
                        Create New Link
                    </button>
                </div>
            </div>

            {/* Links Table */}
            <div className="bg-white rounded-lg shadow overflow-hidden">
                <table className="min-w-full">
                    <thead className="bg-gray-50">
                        <tr>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Link Details
                            </th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Performance
                            </th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Category & Tags
                            </th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Actions
                            </th>
                        </tr>
                    </thead>
                    <tbody className="bg-white divide-y divide-gray-200">
                        {links.map(link => (
                            <tr key={link.id}>
                                <td className="px-6 py-4">
                                    <div className="text-sm font-medium text-gray-900">{link.name}</div>
                                    <div className="text-sm text-gray-500">{link.program}</div>
                                    <div className="text-xs text-gray-400 truncate">{link.affiliateUrl}</div>
                                </td>
                                <td className="px-6 py-4">
                                    <div className="text-sm text-gray-900">{link.clicks} clicks</div>
                                    <div className="text-sm text-green-600">${link.earnings.toFixed(2)} earned</div>
                                    <div className="text-xs text-gray-500">Last click: {link.lastClick}</div>
                                </td>
                                <td className="px-6 py-4">
                                    <div className="text-sm text-gray-900 mb-1">{link.category}</div>
                                    <div className="flex flex-wrap gap-1">
                                        {link.tags.map(tag => (
                                            <span 
                                                key={tag} 
                                                className="px-2 py-1 bg-gray-100 rounded-full text-xs text-gray-600"
                                            >
                                                {tag}
                                            </span>
                                        ))}
                                    </div>
                                </td>
                                <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                                    <button 
                                        className="text-blue-600 hover:text-blue-900 mr-3"
                                        onClick={() => handleCopyLink(link.affiliateUrl)}
                                    >
                                        Copy Link
                                    </button>
                                    <button 
                                        className="text-green-600 hover:text-green-900 mr-3"
                                        onClick={() => {/* Show stats modal */}}
                                    >
                                        View Stats
                                    </button>
                                    <button 
                                        className="text-gray-600 hover:text-gray-900"
                                        onClick={() => {/* Show edit modal */}}
                                    >
                                        Edit
                                    </button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            {/* Quick Stats */}
            <div className="mt-6 grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="bg-white p-4 rounded-lg shadow">
                    <h3 className="text-lg font-medium mb-2">Total Clicks</h3>
                    <p className="text-3xl font-bold text-blue-600">
                        {links.reduce((sum, link) => sum + link.clicks, 0)}
                    </p>
                </div>
                <div className="bg-white p-4 rounded-lg shadow">
                    <h3 className="text-lg font-medium mb-2">Total Earnings</h3>
                    <p className="text-3xl font-bold text-green-600">
                        ${links.reduce((sum, link) => sum + link.earnings, 0).toFixed(2)}
                    </p>
                </div>
                <div className="bg-white p-4 rounded-lg shadow">
                    <h3 className="text-lg font-medium mb-2">Active Links</h3>
                    <p className="text-3xl font-bold text-gray-600">{links.length}</p>
                </div>
            </div>

            {/* Tips */}
            <div className="mt-6 bg-blue-50 rounded-lg p-4">
                <h3 className="font-medium mb-2">Link Management Tips:</h3>
                <ul className="list-disc list-inside text-sm text-gray-600">
                    <li>Use descriptive names for your links to track their purpose</li>
                    <li>Add relevant tags to organize and filter links easily</li>
                    <li>Monitor click-through rates to optimize your content</li>
                    <li>Regularly check for broken or outdated links</li>
                </ul>
            </div>
        </div>
    );
}
