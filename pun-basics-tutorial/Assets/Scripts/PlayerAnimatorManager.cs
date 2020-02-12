using System.Collections;
using System.Collections.Generic;
using Unity.Collections;
using UnityEngine;

namespace Com.MachineApps.Tutorial
{

    public class PlayerAnimatorManager : MonoBehaviour
    {
        #region Private fields

        private Animator animator;

        [SerializeField] 
        private float directionDampTime = 0.25f;

        #endregion


        #region Monobehaviour Callbacks

        // Start is called before the first frame update
        void Start()
        {
            animator = GetComponent<Animator>();
            if (!animator)
            {
                Debug.LogError("PlayerAnimatorManager is missing Animator component", this);
            }
        }

        // Update is called once per frame
        void Update()
        {
            if (!animator)
            {
                return;
            }

            // deal with Jumping
            AnimatorStateInfo stateInfo = animator.GetCurrentAnimatorStateInfo(0);

            // only allow jumping if we are running.
            if (stateInfo.IsName("Base Layer.Run"))
            {
                // When using trigger parameter
                if (Input.GetButtonDown("Fire2"))
                {
                    animator.SetTrigger("Jump");
                }
            }

            float h = Input.GetAxis("Horizontal");
            float v = Input.GetAxis("Vertical");
            if (v < 0)
            {
                v = 0;
            }

            animator.SetFloat("Speed", h * h + v * v);

            //Could also use (it's just to keep values positive):
            //animator.SetFloat("Speed", Mathf.Abs(h) + Mathf.Abs(v));

            animator.SetFloat("Direction", h, directionDampTime, Time.deltaTime);
        }

        #endregion

    }

}