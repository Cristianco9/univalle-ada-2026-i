"use client";

import FileUpload from "@/components/FileUpload";

export default function Home() {
  return (
    <main className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="w-full max-w-xl p-8 bg-white rounded-2xl shadow-lg">
        <h1 className="text-2xl font-bold mb-6 text-center">
          CSV User Sorter
        </h1>
        <FileUpload />
      </div>
    </main>
  );
}