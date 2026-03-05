"use client";

import { motion } from "framer-motion";
import FileUpload from "../components/FileUpload";

export default function Home() {
  return (
    <div className="relative min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-900 via-gray-900 to-black text-white overflow-hidden">

      {/* Animated Background Glow */}
      <div className="absolute w-[500px] h-[500px] bg-purple-600/30 rounded-full blur-[120px] animate-pulse top-[-100px] left-[-100px]" />
      <div className="absolute w-[400px] h-[400px] bg-cyan-500/20 rounded-full blur-[100px] animate-pulse bottom-[-80px] right-[-80px]" />

      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="relative z-10 w-full max-w-2xl p-10 rounded-3xl bg-white/5 backdrop-blur-xl border border-white/10 shadow-2xl"
      >
        {/* Title */}
        <motion.h1
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="text-4xl font-extrabold text-center mb-4 bg-gradient-to-r from-purple-400 via-cyan-400 to-blue-500 bg-clip-text text-transparent"
        >
          CSV User Import System
        </motion.h1>

        {/* Subtitle */}
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.6 }}
          className="text-center text-gray-300 mb-8"
        >
          Upload your CSV file and let the system validate and process your users.
        </motion.p>

        {/* File Upload Component */}
        <motion.div
          whileHover={{ scale: 1.02 }}
          transition={{ type: "spring", stiffness: 200 }}
        >
          <FileUpload />
        </motion.div>
      </motion.div>
    </div>
  );
}