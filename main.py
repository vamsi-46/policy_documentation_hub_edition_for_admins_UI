<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Policy Documentation Hub - Admin</title>
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
            --light-color: #ecf0f1;
            --dark-color: #2c3e50;
            --success-color: #27ae60;
            --warning-color: #f39c12;
            --border-radius: 4px;
            --box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f7fa;
            color: #333;
            line-height: 1.6;
        }

        .container {
            display: grid;
            grid-template-columns: 250px 1fr;
            min-height: 100vh;
        }

        /* Sidebar Styles */
        .sidebar {
            background-color: var(--primary-color);
            color: white;
            padding: 20px 0;
            box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
            position: relative;
            z-index: 10;
        }

        .sidebar-header {
            padding: 0 20px 20px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .sidebar-header h2 {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1.2rem;
        }

        .sidebar-header h2 i {
            color: var(--secondary-color);
        }

        .nav-menu {
            margin-top: 20px;
        }

        .nav-item {
            padding: 12px 20px;
            display: flex;
            align-items: center;
            gap: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            border-left: 3px solid transparent;
        }

        .nav-item:hover {
            background-color: rgba(255, 255, 255, 0.1);
        }

        .nav-item.active {
            background-color: rgba(255, 255, 255, 0.1);
            border-left: 3px solid var(--secondary-color);
        }

        .nav-item i {
            width: 20px;
            text-align: center;
        }

        /* Main Content Styles */
        .main-content {
            padding: 20px;
            overflow-y: auto;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid #ddd;
        }

        .header h1 {
            color: var(--dark-color);
            font-size: 1.8rem;
        }

        .user-info {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .user-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background-color: var(--secondary-color);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
        }

        /* Dashboard Cards */
        .dashboard-cards {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .card {
            background-color: white;
            border-radius: var(--border-radius);
            padding: 20px;
            box-shadow: var(--box-shadow);
            transition: transform 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }

        .card-icon {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }

        .card-icon.policies {
            background-color: var(--secondary-color);
        }

        .card-icon.users {
            background-color: var(--success-color);
        }

        .card-icon.versions {
            background-color: var(--warning-color);
        }

        .card-icon.pending {
            background-color: var(--accent-color);
        }

        .card h3 {
            font-size: 1.1rem;
            color: var(--dark-color);
            margin-bottom: 5px;
        }

        .card p {
            color: #777;
            font-size: 0.9rem;
        }

        .card .count {
            font-size: 2rem;
            font-weight: bold;
            color: var(--dark-color);
        }

        /* Policy Sections */
        .section {
            background-color: white;
            border-radius: var(--border-radius);
            padding: 20px;
            box-shadow: var(--box-shadow);
            margin-bottom: 30px;
        }

        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid #eee;
        }

        .section-header h2 {
            font-size: 1.4rem;
            color: var(--dark-color);
        }

        .btn {
            padding: 8px 16px;
            border: none;
            border-radius: var(--border-radius);
            cursor: pointer;
            font-weight: 500;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }

        .btn-primary {
            background-color: var(--secondary-color);
            color: white;
        }

        .btn-primary:hover {
            background-color: #2980b9;
        }

        .btn-danger {
            background-color: var(--accent-color);
            color: white;
        }

        .btn-danger:hover {
            background-color: #c0392b;
        }

        .btn-outline {
            background-color: transparent;
            border: 1px solid #ddd;
            color: #555;
        }

        .btn-outline:hover {
            background-color: #f5f5f5;
        }

        /* Policy Table */
        .policy-table {
            width: 100%;
            border-collapse: collapse;
        }

        .policy-table th, .policy-table td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #eee;
        }

        .policy-table th {
            background-color: #f8f9fa;
            font-weight: 600;
            color: #555;
        }

        .policy-table tr:hover {
            background-color: #f9f9f9;
        }

        .status-badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
        }

        .status-active {
            background-color: #d4edda;
            color: #155724;
        }

        .status-draft {
            background-color: #fff3cd;
            color: #856404;
        }

        .status-archived {
            background-color: #f8d7da;
            color: #721c24;
        }

        .action-btns {
            display: flex;
            gap: 5px;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .container {
                grid-template-columns: 1fr;
            }

            .sidebar {
                position: fixed;
                width: 250px;
                height: 100vh;
                left: -250px;
                transition: left 0.3s ease;
            }

            .sidebar.active {
                left: 0;
            }

            .mobile-menu-btn {
                display: block;
                background: none;
                border: none;
                font-size: 1.5rem;
                cursor: pointer;
            }
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>
    <div class="container">
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <h2>
                    <i class="fas fa-shield-alt"></i>
                    <span>PolicyHub Admin</span>
                </h2>
            </div>
            <nav class="nav-menu">
                <div class="nav-item active">
                    <i class="fas fa-tachometer-alt"></i>
                    <span>Dashboard</span>
                </div>
                <div class="nav-item">
                    <i class="fas fa-file-alt"></i>
                    <span>All Policies</span>
                </div>
                <div class="nav-item">
                    <i class="fas fa-plus-circle"></i>
                    <span>Create Policy</span>
                </div>
                <div class="nav-item">
                    <i class="fas fa-users-cog"></i>
                    <span>User Management</span>
                </div>
                <div class="nav-item">
                    <i class="fas fa-history"></i>
                    <span>Version History</span>
                </div>
                <div class="nav-item">
                    <i class="fas fa-cog"></i>
                    <span>Settings</span>
                </div>
                <div class="nav-item">
                    <i class="fas fa-sign-out-alt"></i>
                    <span>Logout</span>
                </div>
            </nav>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <div class="header">
                <h1>Policy Documentation Dashboard</h1>
                <div class="user-info">
                    <div class="user-avatar">AD</div>
                    <span>Admin User</span>
                </div>
            </div>

            <!-- Dashboard Cards -->
            <div class="dashboard-cards">
                <div class="card">
                    <div class="card-header">
                        <div>
                            <h3>Total Policies</h3>
                            <p>Active in the system</p>
                        </div>
                        <div class="card-icon policies">
                            <i class="fas fa-file-alt"></i>
                        </div>
                    </div>
                    <div class="count">142</div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div>
                            <h3>Active Users</h3>
                            <p>With access to policies</p>
                        </div>
                        <div class="card-icon users">
                            <i class="fas fa-users"></i>
                        </div>
                    </div>
                    <div class="count">87</div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div>
                            <h3>Policy Versions</h3>
                            <p>Total revisions</p>
                        </div>
                        <div class="card-icon versions">
                            <i class="fas fa-code-branch"></i>
                        </div>
                    </div>
                    <div class="count">326</div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div>
                            <h3>Pending Approvals</h3>
                            <p>Waiting for review</p>
                        </div>
                        <div class="card-icon pending">
                            <i class="fas fa-clock"></i>
                        </div>
                    </div>
                    <div class="count">5</div>
                </div>
            </div>

            <!-- Recent Policies Section -->
            <div class="section">
                <div class="section-header">
                    <h2>Recent Policies</h2>
                    <button class="btn btn-primary">
                        <i class="fas fa-plus"></i>
                        <span>Add New Policy</span>
                    </button>
                </div>
                <table class="policy-table">
                    <thead>
                        <tr>
                            <th>Policy Name</th>
                            <th>Category</th>
                            <th>Last Updated</th>
                            <th>Owner</th>
                            <th>Status</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Data Protection Policy</td>
                            <td>Security</td>
                            <td>2023-10-15</td>
                            <td>John Doe</td>
                            <td><span class="status-badge status-active">Active</span></td>
                            <td>
                                <div class="action-btns">
                                    <button class="btn btn-outline" title="View">
                                        <i class="fas fa-eye"></i>
                                    </button>
                                    <button class="btn btn-outline" title="Edit">
                                        <i class="fas fa-edit"></i>
                                    </button>
                                    <button class="btn btn-outline" title="Archive">
                                        <i class="fas fa-archive"></i>
                                    </button>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td>Remote Work Policy</td>
                            <td>HR</td>
                            <td>2023-09-28</td>
                            <td>Jane Smith</td>
                            <td><span class="status-badge status-active">Active</span></td>
                            <td>
                                <div class="action-btns">
                                    <button class="btn btn-outline" title="View">
                                        <i class="fas fa-eye"></i>
                                    </button>
                                    <button class="btn btn-outline" title="Edit">
                                        <i class="fas fa-edit"></i>
                                    </button>
                                    <button class="btn btn-outline" title="Archive">
                                        <i class="fas fa-archive"></i>
                                    </button>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td>Code of Conduct</td>
                            <td>Compliance</td>
                            <td>2023-08-10</td>
                            <td>Mike Johnson</td>
                            <td><span class="status-badge status-draft">Draft</span></td>
                            <td>
                                <div class="action-btns">
                                    <button class="btn btn-outline" title="View">
                                        <i class="fas fa-eye"></i>
                                    </button>
                                    <button class="btn btn-outline" title="Edit">
                                        <i class="fas fa-edit"></i>
                                    </button>
                                    <button class="btn btn-outline" title="Archive">
                                        <i class="fas fa-archive"></i>
                                    </button>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td>IT Security Policy</td>
                            <td>Security</td>
                            <td>2023-07-22</td>
                            <td>Sarah Williams</td>
                            <td><span class="status-badge status-active">Active</span></td>
                            <td>
                                <div class="action-btns">
                                    <button class="btn btn-outline" title="View">
                                        <i class="fas fa-eye"></i>
                                    </button>
                                    <button class="btn btn-outline" title="Edit">
                                        <i class="fas fa-edit"></i>
                                    </button>
                                    <button class="btn btn-outline" title="Archive">
                                        <i class="fas fa-archive"></i>
                                    </button>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td>Social Media Policy</td>
                            <td>Marketing</td>
                            <td>2023-06-15</td>
                            <td>Robert Brown</td>
                            <td><span class="status-badge status-archived">Archived</span></td>
                            <td>
                                <div class="action-btns">
                                    <button class="btn btn-outline" title="View">
                                        <i class="fas fa-eye"></i>
                                    </button>
                                    <button class="btn btn-outline" title="Edit">
                                        <i class="fas fa-edit"></i>
                                    </button>
                                    <button class="btn btn-outline" title="Restore">
                                        <i class="fas fa-trash-restore"></i>
                                    </button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Pending Approvals Section -->
            <div class="section">
                <div class="section-header">
                    <h2>Pending Approvals</h2>
                    <button class="btn btn-outline">
                        <i class="fas fa-sync-alt"></i>
                        <span>Refresh</span>
                    </button>
                </div>
                <table class="policy-table">
                    <thead>
                        <tr>
                            <th>Policy Name</th>
                            <th>Submitted By</th>
                            <th>Submission Date</th>
                            <th>Changes</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Data Retention Policy</td>
                            <td>Emily Davis</td>
                            <td>2023-10-18</td>
                            <td>Major revisions</td>
                            <td>
                                <div class="action-btns">
                                    <button class="btn btn-primary" title="Approve">
                                        <i class="fas fa-check"></i>
                                    </button>
                                    <button class="btn btn-danger" title="Reject">
                                        <i class="fas fa-times"></i>
                                    </button>
                                    <button class="btn btn-outline" title="Review">
                                        <i class="fas fa-search"></i>
                                    </button>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td>Travel Expense Policy</td>
                            <td>David Wilson</td>
                            <td>2023-10-17</td>
                            <td>Minor updates</td>
                            <td>
                                <div class="action-btns">
                                    <button class="btn btn-primary" title="Approve">
                                        <i class="fas fa-check"></i>
                                    </button>
                                    <button class="btn btn-danger" title="Reject">
                                        <i class="fas fa-times"></i>
                                    </button>
                                    <button class="btn btn-outline" title="Review">
                                        <i class="fas fa-search"></i>
                                    </button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </main>
    </div>

    <script>
        // Simple script for mobile menu toggle (would be expanded in a real implementation)
        document.addEventListener('DOMContentLoaded', function() {
            // This would be used to toggle the mobile menu in a real implementation
            const mobileMenuBtn = document.createElement('button');
            mobileMenuBtn.className = 'mobile-menu-btn';
            mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
            mobileMenuBtn.onclick = function() {
                document.querySelector('.sidebar').classList.toggle('active');
            };
            
            // In a real app, we would conditionally add this only for mobile
            document.querySelector('.header').prepend(mobileMenuBtn);
        });
    </script>
</body>
</html>