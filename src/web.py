<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>
   TruthWeb Browser
  </title>
  <script src="https://cdn.tailwindcss.com">
  </script>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&amp;display=swap" rel="stylesheet"/>
 </head>
 <body class="bg-gray-900 text-gray-100 font-roboto">
  <div class="container mx-auto p-4">
   <div class="flex items-center justify-between mb-4 bg-gray-800 p-2 rounded shadow">
    <div class="flex space-x-2">
     <button class="bg-gray-700 p-2 rounded" id="backBtn">
      <i class="fas fa-arrow-left text-xl text-gray-100">
      </i>
     </button>
     <button class="bg-gray-700 p-2 rounded" id="forwardBtn">
      <i class="fas fa-arrow-right text-xl text-gray-100">
      </i>
     </button>
     <button class="bg-gray-700 p-2 rounded" id="refreshBtn">
      <i class="fas fa-sync text-xl text-gray-100">
      </i>
     </button>
     <button class="bg-gray-700 p-2 rounded" id="homeBtn">
      <i class="fas fa-home text-xl text-gray-100">
      </i>
     </button>
    </div>
    <div class="flex flex-grow mx-2">
     <input class="border p-2 w-full rounded-l bg-gray-700 text-gray-100" id="url" placeholder="Search Google or type a URL" type="text"/>
     <button class="bg-blue-500 text-white p-2 rounded-r" id="goBtn">
      <i class="fas fa-arrow-right">
      </i>
     </button>
    </div>
    <div class="flex space-x-2">
     <button class="bg-gray-700 p-2 rounded" id="stopBtn">
      <i class="fas fa-times text-xl text-gray-100">
      </i>
     </button>
     <button class="bg-gray-700 p-2 rounded" id="settingsBtn">
      <i class="fas fa-cog text-xl text-gray-100">
      </i>
     </button>
    </div>
   </div>
   <div class="w-full bg-gray-800 p-4 rounded shadow">
    <iframe class="w-full h-96 border p-2 bg-gray-900 text-gray-100" id="webContent" src="">
    </iframe>
   </div>
  </div>
  <script>
   function openUrl(url) {
            document.getElementById('webContent').src = url;
        }

        function go() {
            const url = document.getElementById('url').value;
            document.getElementById('webContent').src = url;
        }

        function clearText() {
            document.getElementById('webContent').src = '';
        }

        function clearEntry() {
            document.getElementById('url').value = '';
        }

        function goHome() {
            document.getElementById('webContent').src = 'https://www.google.com';
        }

        document.getElementById('goBtn').addEventListener('click', go);
        document.getElementById('backBtn').addEventListener('click', () => window.history.back());
        document.getElementById('forwardBtn').addEventListener('click', () => window.history.forward());
        document.getElementById('refreshBtn').addEventListener('click', () => location.reload());
        document.getElementById('stopBtn').addEventListener('click', clearText);
        document.getElementById('homeBtn').addEventListener('click', goHome);
  </script>
 </body>
</html>
