import { useState } from 'react'
import './App.css'

interface FormData {
  email: string;
  course: string;
  startHour: string;
  endHour: string;
}

function App() {
  const [form, setForm] = useState<FormData>({
    email: '',
    course: '',
    startHour: '0',
    endHour: '23',
  })
  const [message, setMessage] = useState('')

  const hours = Array.from({ length: 24 }, (_, i) => i)
  const courses = ['Course A', 'Course B', 'Course C']

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target
    setForm((prev) => ({ ...prev, [name]: value }))
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setMessage('Submitting...')
    try {
      const res = await fetch('/subscribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      })
      if (res.ok) {
        setMessage('Subscription saved!')
        setForm({ email: '', course: '', startHour: '0', endHour: '23' })
      } else {
        setMessage('Error submitting form')
      }
    } catch (err) {
      setMessage('Error submitting form')
    }
  }

  return (
    <div className="container">
      <h1>Tee Time Alerts</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <input
            type="email"
            name="email"
            placeholder="Enter your email"
            value={form.email}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <select name="course" value={form.course} onChange={handleChange} required>
            <option value="" disabled>Select course</option>
            {courses.map((c) => (
              <option key={c} value={c}>{c}</option>
            ))}
          </select>
        </div>
        <div className="hour-selects">
          <select name="startHour" value={form.startHour} onChange={handleChange} required>
            {hours.map((h) => (
              <option key={h} value={h}>{h}:00</option>
            ))}
          </select>
          <span>to</span>
          <select name="endHour" value={form.endHour} onChange={handleChange} required>
            {hours.map((h) => (
              <option key={h} value={h}>{h}:00</option>
            ))}
          </select>
        </div>
        <button type="submit">Subscribe</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  )
}

export default App
