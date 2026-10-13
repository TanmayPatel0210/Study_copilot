"use client";

import { useState } from "react";
import { generateStudyMaterials, StudyPackage } from "@/lib/api";

export default function DashboardPage() {
  const [studyText, setStudyText] = useState("");
  const [gradeLevel, setGradeLevel] = useState("college");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [studyPackage, setStudyPackage] = useState<StudyPackage | null>(null);

  const handleGenerate = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!studyText.trim()) return;

    setLoading(true);
    setError(null);

    try {
      const data = await generateStudyMaterials(studyText, gradeLevel);
      setStudyPackage(data);
    } catch (err: any) {
      setError(err.message || "An unexpected error occurred.");
    } finally {
      setLoading(false);
    }-slate-800 bg-slate-900/60 p-4 backdrop-blur-sm">
            <span className="text-xs text-slate-400 font-medium">Total Study Sessions</span>
         
  };

  return (
    <div className="max-w-6xl mx-auto space-y-8">
      {/* Welcome Hero Banner */}
      <div className="rounded-3xl border border-indigo-500/20 bg-gradient-to-r from-indigo-950/30 via-slate-900/50 to-slate-900/80 p-8 shadow-2xl relative overflow-hidden">
        <div className="absolute right-0 top-0 translate-x-8 -translate-y-8 h-64 w-64 rounded-full bg-indigo-500/10 blur-3xl pointer-events-none"></div>
        <h2 className="text-2xl lg:text-3xl font-extrabold text-white tracking-tight">
          Welcome back to MindForge 🚀
        </h2>
        <p className="mt-2 text-sm text-slate-400 max-w-2xl leading-relaxed">
          Transform your study materials into interactive flashcards and smart quizzes instantly. Paste your notes below to let Gemini generate your custom study package.
        </p>

        {/* Quick Stats Grid */}
        <div className="mt-8 grid grid-cols-1 sm:grid-cols-3 gap-4">
          <div className="rounded-2xl border border