function ApplicationStatus() {
    const [applications, setApplications] = useState([
        {
            id: 1,
            programName: "Amazon Associates",
            status: "pending",
            dateApplied: "2024-12-20",
            nextAction: "Complete profile",
            nextActionDue: "2024-12-28",
            notes: "Need to add more content to blog",
            loginUrl: "https://affiliate-program.amazon.com/",
            credentials: { username: "myemail@example.com" }
        },
        {
            id: 2,
            programName: "Shopify Partners",
            status: "approved",
            dateApplied: "2024-12-15",
            nextAction: "Create first link",
            nextActionDue: "2024-12-30",
            notes: "Approved on 12/22. Commission rate: 200% first 2 months",
            loginUrl: "https://partners.shopify.com/",
            credentials: { username: "myemail@example.com" }
        }
    ]);

    const statusColors = {
        pending: "bg-yellow-100 text-yellow-800",
        approved: "bg-green-100 text-green-800",
        rejected: "bg-red-100 text-red-800",
        inactive: "bg-gray-100 text-gray-800"
    };

    const handleStatusChange = (id, newStatus) => {
        setApplications(apps => 
            apps.map(app => 
                app.id === id ? { ...app, status: newStatus } : app
            )
        );
    };

    const handleNoteUpdate = (id, newNote) => {
        setApplications(apps => 
            apps.map(app => 
                app.id === id ? { ...app, notes: newNote } : app
            )
        );
    };

    return (
        <div className="p-6">
            <div className="mb-6 flex justify-between items-center">
                <h1 className="text-2xl font-semibold">Application Status</h1>
                <button 
                    className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
                    onClick={() => {/* Add new application logic */}}
                >
                    New Application
                </button>
            </div>

            {/* Applications Table */}
            <div className="bg-white rounded-lg shadow overflow-hidden">
                <table className="min-w-full">
                    <thead className="bg-gray-50">
                        <tr>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Program
                            </th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Status
                            </th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Applied Date
                            </th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Next Action
                            </th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Notes
                            </th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Actions
                            </th>
                        </tr>
                    </thead>
                    <tbody className="bg-white divide-y divide-gray-200">
                        {applications.map(app => (
                            <tr key={app.id}>
                                <td className="px-6 py-4 whitespace-nowrap">
                                    <div className="text-sm font-medium text-gray-900">
                                        {app.programName}
                                    </div>
                                </td>
                                <td className="px-6 py-4 whitespace-nowrap">
                                    <span className={`px-2 py-1 rounded-full text-xs ${statusColors[app.status]}`}>
                                        {app.status.charAt(0).toUpperCase() + app.status.slice(1)}
                                    </span>
                                </td>
                                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                    {app.dateApplied}
                                </td>
                                <td className="px-6 py-4 whitespace-nowrap">
                                    <div className="text-sm text-gray-900">{app.nextAction}</div>
                                    <div className="text-xs text-gray-500">Due: {app.nextActionDue}</div>
                                </td>
                                <td className="px-6 py-4">
                                    <textarea 
                                        className="text-sm text-gray-500 w-full border rounded p-2"
                                        value={app.notes}
                                        onChange={(e) => handleNoteUpdate(app.id, e.target.value)}
                                    />
                                </td>
                                <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                                    <button 
                                        className="text-blue-600 hover:text-blue-900 mr-3"
                                        onClick={() => window.open(app.loginUrl, '_blank')}
                                    >
                                        Login
                                    </button>
                                    <button 
                                        className="text-green-600 hover:text-green-900"
                                        onClick={() => {/* Show credentials modal */}}
                                    >
                                        View Login
                                    </button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            {/* Quick Tips */}
            <div className="mt-6 bg-blue-50 rounded-lg p-4">
                <h3 className="font-medium mb-2">Application Tips:</h3>
                <ul className="list-disc list-inside text-sm text-gray-600">
                    <li>Keep your profile information consistent across programs</li>
                    <li>Set reminders for following up on pending applications</li>
                    <li>Store login credentials securely</li>
                    <li>Track important dates and deadlines</li>
                </ul>
            </div>
        </div>
    );
}
