<?php
    $title = "AIS2 Junior Uncofficial Website";
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>AIS2 Junior Unofficial Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <nav>
        <h1>AIS2 Junior 舊型態高中職資安課程</h1>
    </nav>
    <main>
        <h2>歡迎來到 AIS2 Junior 的非官方網站！</h2>
        <p>不是真的 AIS3 Junior 網站。</p>
        <div class="usercomponent">
            <h3>助教</h3>
            <div class="userdiv" id="tas">
            </div>

            <h3>個人贊助</h3>
            <div class="userdiv" id="sponsors">
            </div>
        </div>
    </main>

    <script>
        async function loadUsers() {
            try {
                const response = await fetch('config.json');
                const userList = await response.json();
                const userIds = userList.user;
                
                const users = [];
                for (const userInfo of userIds) {
                    const userId = userInfo.id;
                    try {
                        const userResponse = await fetch(`users/${userId}`);
                        const userDetail = await userResponse.json();
                        users.push(userDetail);
                    } catch (error) {
                        console.error(`無法載入用戶 ${userId} 的資料:`, error);
                    }
                }
                
                displayUsers(users);
                
            } catch (error) {
                console.error('載入用戶列表失敗:', error);
            }
        }
        
        function displayUsers(users) {
            const tasContainer = document.getElementById('tas');
            const sponsorsContainer = document.getElementById('sponsors');
            
            tasContainer.innerHTML = '';
            sponsorsContainer.innerHTML = '';
            
            users.forEach(user => {
                console.log(user);
                const userElement = createUserElement(user);
                
                if (user.type === 'ta') {
                    tasContainer.appendChild(userElement);
                } else if (user.type === 'sponsor') {
                    sponsorsContainer.appendChild(userElement);
                }
            });
        }
        
        function createUserElement(user) {
            const userDiv = document.createElement('div');
            userDiv.className = 'user';
            
            const img = document.createElement('img');
            img.src = user.img;
            img.alt = user.name;
            
            const p = document.createElement('p');
            p.textContent = user.name;
            
            userDiv.appendChild(img);
            userDiv.appendChild(p);
            
            return userDiv;
        }
        
        document.addEventListener('DOMContentLoaded', loadUsers);
    </script>
</body>
</html>
